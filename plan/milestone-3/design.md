# Milestone 3. Core Features Implemented - Design

## PROJECT INFO
* [Software Project Plan - Capture](https://capture350.herokuapp.com/)

* Other Roles - [Requirements.md](requirements.md), [Design.md](design.md), [Code.md](code.md), [Test.md](test.md)

* File: milestone-3/design.md

* URL: https://github.com/Adam1400/cs350/blob/master/plan/milestone-3/design.md

### Milestone 3. Core Features Implemented

Role: Designer - Design
 
Goal: Component Design - API
* Prototype - development spike of core functionality
* Implement data models
* Implement views
* Implement URL routes

## Capture - Component Design - API

### Prototype - development spike of core functionality
* Core set features for this project:
    * Users can register an account and edit account username/password
    * Users can see their feed
    * Users can create and edit a post 
    * Users can make comments and like posts
### Implement data models
* Data models include Users, Profiles, Posts, and Feed
#### Users
* username
* password
* profile*

#### Profiles
* name
* username
* bio
* edit profile
* posts*
#### Posts
* username
* image
* caption
* comment
* like

#### Feed
* posts*
* order

Data models: (https://github.com/Adam1400/cs350/blob/master/capture/post/models.py)
### Implement views
* The the views that we have implemented so far post list view and post view

### Implement URL routes