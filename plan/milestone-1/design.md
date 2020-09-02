# Milestone 1. Project Plan

## Role: Designer - Design - Allen Adams

### Goal: Version control / django setup basics / Determine hosting/ technologies

* Setup Github account
* Download Github Desktop
* Clone main repo
* Download IDE (Visual Studio Code) 
* Download Python3 (Latest version)
* Watch this video to learn basics: https://www.youtube.com/watch?v=UmljXZIypDc
* Select Development Tools
* Infrastructure - Frameworks & Tools
* Setup Guide
* Decide on App deployment

---
### UPDATE | 9-4-2020

#### (ALL) complete
* ~~Setup Github account~~
* ~~Download Github Desktop~~
* ~~Clone main repo~~
* ~~Download IDE (Visual Studio Code)~~
* ~~Download Python3 (Latest version)~~
* ~~Watch this video to learn basics: https://www.youtube.com/watch?v=UmljXZIypDc~~
* ~~Select Development Tools~~
  * VS CODE for ide
  * git bash (or git desktop)
* ~~Infrastructure - Frameworks & Tools~~
  * DJANGO framework
  * GITHUB
  * HTML / CSS / JAVASCRIPT
* ~~Setup Guide~~
  * Everyone is set up
* ~~Decide on App deployment~~
  * Hosting through Heroku (see readme)
  
### VS CODE
Going with vs code because it handles several languages at once. We will be ballancing Python, html, css, and perhaps JS all in one app. To meet our needs we needed an IDE that can handel our diverse platform. VS code has git intigration, this will let us track and push our changes easily.

### git bash (optional)
VS code and git go hand and hand. Although its not requirede for VS code, having git bash will allow for better version controll intigration. Git dektop alone does not intigrade with vs code. 

### DJANGO Framework
Choosing django for its simplicity in testing and deployment. Django compared to node.js requires less overhead and better suits our needs on this project.

#### Overhead
* python envnviorment IS REQUIRED for local testing and is not included in repo (becuase its too big)
* to set up a python ENV (enviorment)
 * install latest version of python (3.7)
 * in command-line change current directory to capture directory (in terminal --> cd documents/github/cs350/capture)
 * to create envirorment type --> python -m venv env
 * install django, type --> python install django 
 * IN FUTURE you may need to install other things.... See [dependencies](https://github.com/Adam1400/cs350/blob/master/capture/requirements.txt) for further installs and enviornment set up.
 * when testing or before writing code activate env, type --> env\Scripts\activate.bat
 * then to test page in browser type (still in capture directory) --> python manage.py runserver
 * to view in browser go to --> localhost:8000 
 * in comandline press CTRL + C to exit testing 
 

### GITHUB
Using github to mannage version control. The main repo was created on my (Allen's) github page. Each member of the team was added as a contributor and cloned the master repo.

### HTML / CSS / JAVASCRIPT
Using the standard web dev platorm through django. However, i'm conidering using PUG as our view engine... it might make things more consistant accross langiages (python in particular). Give update on this in week 2.

### HOSTING
We are using heroku as I was already firmilar with this platform. At this point in time the app is deployed and hosted through my heroku account (Allen). In the future we may want to all be made contributors on heroku. Will update this by week 2. 


