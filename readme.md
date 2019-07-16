# Mars Mission App

### **Objective :**

All about Mars - an app to show the latest news, facts, weather, the hemispheres.

 

### **Author :**

Emily Mo

 

### **About the data :**

Webscraping is used to get : 

- the latest featured image of Mars from https://www.jpl.nasa.gov/spaceimages/?search=&category=MarsIt,

- the latest weather on Mars from https://twitter.com/marswxreport?lang=en,

- Mars facts from http://space-facts.com/mars/ and convert the information into an HTML table, 

- and the Mars hemispheres photos from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars.

  

### **About the app :**

This app first retrieves information about the data webscraped from the last time the app was opened.  The data is stored in Mongo database.  If the app is called locally, the local Mongo database will be obtained, or else, it will be fetched from Heroko Mongo (add-on).  If the button in the middle of the page is clicked, the information will be scraped afresh from the websites mentioned in ***About the data***

- HTML/CSS/Bootstrap
- flask app (python)
- webscraping - beautiful soup / selenium / splinter / requests
- flask pyMongo 
- Mongo database 
- and json format.  



### Deployment :**

This app is deployed in Heroku and it can be checked out here : 

[https://mars-mission-app.herokuapp.com](https://mars-mission-app.herokuapp.com/)