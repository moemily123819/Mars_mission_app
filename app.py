from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app = Flask(__name__,
            static_url_path='',
           static_folder='static')

MONGO_URI = os.environ.get('MONGODB_URI')
#GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN')
#CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')

if not MONGO_URI:
    MONGO_URI = "mongodb://localhost:27017/mars_mission_app";


app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

#chrome_options = Options()
#chrome_options.binary_location = GOOGLE_CHROME_BIN
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--no-sandbox')
#driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
