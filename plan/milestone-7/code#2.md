# Milestone 7. Gather and Implement Feedback
## Role: Coder 2 - Code - Allen Adams

### Goal: Implement user feedback!

* Address Issues
* Reply to all
* Delete Post
* Fix Scaling
* Alter Animation timings
* Imporove navbar 
* Fix timestamps
* Resolve sign in bug
* Address unmet issues...
* Future Endeavors? 

### UPDATE | 11-30-2020

#### (ALL) complete
* ~~Address Issues~~
* ~~Reply to all~~
* ~~Delete Post~~
* ~~Fix Scaling~~
    * Somewhat resolved
* ~~Alter Animation timings~~
* ~~Imporove navbar~~ 
* ~~Fix timestamps~~
* ~~Resolve sign in bug~~
* ~~Address unmet issues...~~
    * Bound by time constraints
* ~~Future Endeavors?~~ 

### Issues and Replies
I have seen all issue posts and have replied to each one of them. Thank you everyone for your feedback! If you have any more questions, comments or issues let me know [here](https://github.com/Adam1400/cs350/issues). To look at resolved issues look over [here](https://github.com/Adam1400/cs350/issues?q=is%3Aissue+is%3Aclosed). 

### Delete Posts
You can now delete your own posts! Thanks to hart2533 for the [suggestion](https://github.com/Adam1400/cs350/issues/13). To delete a post make sure your signed in to the account you posted your photo from. Then click on the post you want to delete (on the main page). Scroll to the bottom and click delete!

### Fixed Scaling
Several users commented that scaling was a big issue for them. Some said the pictures were larger than their screen and others said that pictures were too big and causing lag. In terms of whats been changed, pictures now have a max height of 45rem. Pictures will now scale better to your device. They should fit within the height of your max browser size. However, if after testing this is not the case on your device let me know! In terms of slow loading times, this could be caused by amazon s3... However, just know we do not compress the pictures. Reducing the max size may help in the browser. However, there were too manny hoops to jump through to get s3 to auto scale the uploaded pics. I would need to implement a lambda function that handels compresson on the server side and I dont think I can finish that before the end of class. Perhaps in the future I will add this (outside of cs350.. stay tuned).

### Animations
In addition to new scaling features... Picture animations have been reworked as well. Before, hovering over a picture would expand it emediatly. At the [sugestion](https://github.com/Adam1400/cs350/issues/5) of SProv7615 animations now have an idel time before playing. Users were complainging that scolling was annoying with the pictures expaning as you go. Now pictures will not scale up unless you hover for 1.5 seconds. 

### Navbar Update
At the [suggestion](https://github.com/Adam1400/cs350/issues/11) of KevinBRitter, the navbar is more intuitive. As you progress acorss mages the navbar will remain static. There will always be a home and post button in the navbar. This should make it esier to navigate around the site. 

### Timestamps
Thom1664 [notified](https://github.com/Adam1400/cs350/issues/9) me that post times were about 7 hours ahead. This was remidied by setting the timezone. Posts are govertned by Denver mountain time.  

### Sign in Problem
Several users notified me that when they attmepted to like a post (without creating an account)... they would be redirected to the sigh up screen. Upon created an account the app would attempt the bring them back to the post detail they were on. The issue here was the we were not passing the primary key though though the sign up to properly fetch the detail. To fix this I made the sign up page return them to the main screen insead of attempting to redicect to a previous screen. 

### Unresolved issues and sugesstions
All major prolems were fixed. However, some user suggestions have not been implemented due to time constraints. Manny users wanted features ported from instagram. This includes things like, an explore section, user stories (temporaty posts), popular posts page, and client side picture cropping. These were not implemented for 1 of 3 reasons. 
* 1) I would not be able to finish it by the end of milestine 7. 
* 2) We want to differentiate ourself from instagram. 
* 3) This feature was already redacted/ determined by a previous design desicion. 

For those requesting an explone section, thats what the purpose of the main page is for. Here, you are able to see all user posts and explore at your leasure. In the future I may add a popular post section though! 

### Future Endeavors
This will be the last milestone for the purpose of cs350... However, this does not mean development will stop. Sense I manage the site, I will continue to support this application! (if anyone cares)... When I add featurs I will make a post on the site. I will be incliding this as part of my development portfolio. Hopfuly it will help get me hired somewhere! 
