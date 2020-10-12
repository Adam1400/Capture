# Milestone 3. Core Features Implemented

## Role: Test - Allen Adams

### Goal: Test Pages/ Templates and Data

* implement automated tests
* Test Main page functionality
* Test Post Page functionality
* Assert 404 Error handles 
* Test invalid data
* Make tests for local env and on heroku 

### UPDATE | 9-30-2020

#### (ALL) complete
* ~~implement automated tests~~
    * See tests.py under posts
    * Tested 404 errors when template fails to load
    * 3 Failures on index, post and admin
* ~~Test Main page functionality~~
    * Page is functioning properly and will scale pictures to container
    * works on mobile
* ~~Test Post Page functionality~~
    * This page works, but post button has yet to be set up (expected)
    * Footer navbar properly switches between post page and home page
    * works on moble... top margin is messed up though
* ~~Assert 404 Error handles~~
    * Currently there is no redirect page for a 404 error
    * Will need to add this page in future update
* ~~Test invalid data~~
    * Invalid data tests were a sucess
    * Invalid data will not populate main page
    * need to set defaults in this case (when data is null/ invalid)
* ~~Make tests for local env and on heroku~~
    * Heroku is a pain to work with
    * Currently the database does not work on heroku
    * At some point need to est AWS S3 buckets to hold static files
    * Pages are working, database is not

### Automated Tests
A few tests have been established in tests.py. These test assess 404 errors when either the user goes to a non existant page... or when one of the templates fail. To run tests => python manage.py test . The user should be given a 404 error when acessing an unavailable page. The user should see a 404 error when a template fails to load. These cases ae working however, in the future we need to make a 404 page template instead of using default. This page should redirect the user back to the home page. 3 Failures arise from automated tests because we have no 404 error template. Turning debug mode off should fix this and prompt the default django 404. In the future make sure to turn off debug for deployment.

### Main Page Functionality
Evrything is working on the main page. Pictures are scaling properly to 75% of the container size. This model makes portrate pictures appear much larger than landscape. May want to set different conditions for these types of pictures in the future. Mobile works as well and pictures/ text scale properly. 

### Test Page Functionality/ Nav Bar Footer
This page works for the most part, the templates are poplulating the page... However there is a scaling issue on mobile that will need to be fixed (use percentage for margin top instead of br tags). Post button does not work yet, but this was expected for now. Input boxes work fine, but in the future need error handeling on the backend for security. Navbar works properly and switches between the main page and post.

### 404 Errors
Although all app pages are working properly we will need a 404 page in the future. Currently django is yelling at us because we dont have one. This is because debug mode is turned on. Turn it off in the future.

### Data Tests
Now that the database has been established, it was tested using bad data. Ultimatly the site handeled bad data well... for instance giving the database an invalid date will result in the main page not posting the date. This is ideal... we would rather the site not handel bad data than accept it and try to work with it. Furtheremore there are some checks in play that ensure the backend accepts the right type of data. For instance the pictures field will only accept urls. In the future we may want to set picture and text defualts if data is null or is bad.

### Heroku Headache...
Although all pages are working on heroku there are some major issues with deployment. Heroku does not serve static files and will want us to host those files elsewhere. We can use AWS S3 buckets to hold data in the future... However this is snowballing into a mess. In hindsight we shouldve hosted elsewhere. Heroku is more work than expected. Currently the database is not working and neither is css. Our temporoary workaround for data is populating the main page with dummy data. Our workaround for css is putting all css in style tags. Although this will work in the short run it is not sustainable. Waiting to see how other teams handel this propblem as well. We are atleat 3 weeks ahead of any other team so thats gonna take a while. 

### New Objectives For Programer
* Make 404 page (turn off debug durring deployment)
* Realign post fields on the post page
* Set data defualts in null conditions
* Work with tester/ Designer to find static file solution on heroku

### New Objectives for Designer
* Establish a AWS S3 bucket and link it to our app
* Work with tester/ Programer to find static file solution on heroku
