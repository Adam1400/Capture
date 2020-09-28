# Milestone 1. Project Plan

## PROJECT INFO
* [Software Project Plan - Capture](https://capture350.herokuapp.com/)

* Other Roles - [Requirements.md](requirements.md), [Design.md](design.md), [Code.md](code.md), [Test.md](test.md)

* File: Milestone-1/test.md

* URL: https://github.com/Adam1400/cs350/blob/master/plan/milestone-1/test.md
## Role: QA Engineer - Test

### Goal: Version control / django setup basics / Testing standards

* Setup Github account
* Download Github Desktop
* Clone main repo
* Download IDE (Visual Studio Code) 
* Download Python3 (Latest version)
* Watch this video to learn basics: https://www.youtube.com/watch?v=UmljXZIypDc
* Outline of testing that will be used
* Setup structure for testing
* Log issues
* Document how to log issues

## Capture - Test Plan

Each level of the hierarchy produces increasing levels of detail.  Test planning should always start at the top and work down. This prevents getting lost
in the weeds and running out of time.

A typical medium-sized app can be built in about 1000 hours of engineering time.  This means that about 250 hours should be spent on testing.  The
testing hierarchy acts as a natural budget for how to spent that time.


### Testing Levels 

#### Level 1 - Test Plan

* High level discussion of testing strategy
* Outline the major types of testing that will be done
    * Manual Acceptance Testing - A person uses the application and observes what happens.  The test script describes scenarios that the tester must go through.
    * Django unit test - Automatic tests that may start with a blank database.  These tests can be very fine grained or run the entire system.
    * Hammer test - These tests execute automatic scenarios that exercise the entire system.
    * Quick test - The test is only used during development to iterate on a single function.
    * Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing.
    * Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements.
    
Capture testing

* Testing will be reduced because of limited time on this project.
* Essential testing will include
    * Manual Acceptance Testing
    * Quick Tests in development
    * Page Tests (using "requests" Python package on PyTest)
    

#### Level 2 - Test Area

* This level outlines the testing that will occur on each major block of functionality.
* Product subsystems
    * Views
    * Database
    * Order processing
    * User accounts
    * Reports
    * Diagnostics

#### Level 3 - User Story Test

* Each Test Area is decomposed into a number of User Stories.  
* Each User Story is defined as a User Experience (UX) that is documented in the requirements
* A User Story Test outlines how the UX scenario will be exercised and verified
* Examples:  User Account UX,  Create Post UX, Create News Feed UX

#### Level 4 - Test Script

* Each User Story  is decomposed into a number of User Scenarios.  
* A Test Script outlines how the User Scenario will be exercised and verified.
* Examples:  User UX
    * User can register
    * User can login
    * User can logout
    * Only users can interact with content and all the features

#### Level 5 - Test Case

* Each User Scenarios  is decomposed into a number of specific features that the app implements.  
* A Test Case outlines specific behavior to be exercised and what the expected results are.
* Examples:  User can register
    * Successful registration
    * Error for bad email, name, password, or already have an account
    * User can login after registering
    * Errors prevent user from creating an account


## Hierarchy of Test Details

### Complete Test Plan

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (7-10)
* Level 3 - User Story Tests (50-100)
* Level 4 - Test Scripts (200-400)
* Level 5 - Test Cases (1000-2000)

### Essential Test Plan

This task can seem overwhelming if you look at the whole.   We will be using a essential planning strategy at the start of the project to focus on the core testing first.  If we have time later we can add in more testing.

While every item in the hierarchy may have 5-10 legitimate children, they are not all equally important.  Our essential test plan forces us to select the four most important items at every level.  This gives a robust plan for test what is truly important.  Compare the number of artifacts to the complete plan above.  Instead of detailing 2000 Test Cases we are only dealing with 250.

Picture Builder Testing Hierarchy

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (4)
* Level 3 - User Story Tests (16)
* Level 4 - Test Scripts (64)
* Level 5 - Test Cases (256)

Over the course of the project we plan to spend about 250 hours testing and can focus on the 250 Essential Test Cases.  This makes testing totally predictable and manageable.  If there is enough time you can do more but you are guaranteed to get the most important stuff tested.


## User Auth - Test Script

Manual Testing - live user clicking buttons

Test Cases - User Auth

* Scenario 1 - Guest Access
    * Guests can see system and view specific content
    * Not logged in displayed
    * Guest cannot comment and see other peoples post
    * Menu has links to register, log in, and home page
    * Menu has a search bar

* Scenario 2 - Register New User
    * User can register
    * Error for used email
    * New users are created
    * Dropping a user account removes the user record
    * Existing user records are used

* Scenario 3 - User Access
    * User can log in successfully
    * User can see their news feed and access content
    * Account name displayed
    * Logout menu item
    * Menu has links to Home Page, Account Page, Recent Activity, and Add Content
    * Home Page takes users to news feed
    * Account Page shows users their account info and all their posted content
    * Recent Activity shows users recent content that they have interacted with
    * Add Content lets users add content for other users to see
    * Dropped users can not log in


### Setup structure for testing

The capture project will start by doing manual testing only.  This means for the
first two milestones we do not need to have any specific infrastructure for automated
testing.

The above test scripts cover the scope and high level direction that the testing will 
take.  An example Level 4 - Test Script has been included to illustrate the kind of 
Test Scripts that will be developed later on in the project.

A desicion for documenting tesing for all five levels is still being decided and will be posted here once the decision is made.

### Log issues

The Product Backlog will be an Issue in the Capture project.  It will track the 
priorities for the current Sprint.  The functionality that is expected for the next
milestone will be documented in the Product Backlog.

At the end of the Milestone all work listed in the Product Backlog must be complete.
Any unresolved issues must be logged within the Github issues list.

