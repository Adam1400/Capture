# Milestone 2. Technology Proven

## Role: Programmer - Code - Allen Adams

### Goal: Test-driven development workflow 

* Populate main capture page
* Introduce test data
* Display data on main page
* Apply CSS styles
* Establish and make preperations for "Post" page
* make sure everything still runs on heroku

### UPDATE | 9-18-2020

#### (ALL) complete
* ~~Populate main capture page~~
* ~~Introduce test data~~
    * Added two samples of test data
    * Spoofed the pictures for now
    * Pictures are invoked via http links (google images)
* ~~Display data on main page~~
    * Applyed simple layout
    * User on top => picture => date => comment
* ~~Apply CSS styles~~
    * Heroku does not compile static files properly
    * CSS works on local host but on heroku
    * solution: make a view containing just CSS incapsulated in style tags
    * extend base layout in header to include this CSS view
    * works fine for now... in the future may want to configure for heroku
* ~~Establish and make preperations for "Post" page~~
    * Post page view exists... for now put => /post in url to see this page
    * New update contains a nav bar that can point to post page
    * (Have not pushed this to heroku at this time)
* ~~make sure everything still runs on heroku~~
    * everything works fine on heroku (asside form static css => found teporary solution)

### TEST DATA
For initial testing and proof of concept, data is stored in a dictionary that is then invoked through the index view. Althought the text works fine, for our app we need pictures... so for now our data contains links to images sources rather than an uploaded picture. From here we set that link as a veriable and pass it into the source of an image tag. This will be similar to how things will work with uploaded images... the link will be the path and it will point to a folder with the uploaded pictures. So for a proof of concept this data is perfect.   

### POPULATE MAIN PAGE
To just get things of the starting line I just centred all content and placed it in a order that resembles instagram. I seperated each bost by an line. 

### APPLY CSS
Using bootstrap to make things look more professional. From here custom css is currently being envoked through a html template... this is because heroku has issues with static files. So for now apply css under Post/templates/post/style.html 

### POST PAGE
A route and view exist for this page but currently there is now navigation to get there. Maualy put in /post too see this view. Currently there is nothing on it. However on the local side of things there exists a navbar to change between the two pages (main and post) so look out for that in the future.

### HEROKU UPDATE
It turns out heroku has alot of extra overhead in getting static files to work.... this may prove to be extremly bad when uploading static pictures files. uh oh! I've herd some people say that heroku does not support upload files... so the capture app might have blown up on the runway. However, based on our proof of concept we know that image sources will still work. So hope is not lost. I'll give more updates on this in the future. 

