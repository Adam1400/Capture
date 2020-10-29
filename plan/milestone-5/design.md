# Milestone 5. Tests Complete

## Role: Designer - Design - Allen Adams

### Goal: Intigrate AWS S3 buckets / address security issues

* Setup AWS account
* Create S3 bucket
* Create AWS admin
* intigrade with app
* See env var problem
* Make pictures an upload instead of reference address url
* Address database migrations


### UPDATE | 10-29-2020

#### (ALL) complete
* ~~Setup AWS account~~
    * Under my account
* ~~Create S3 bucket~~
    * Created and hosted on us-east-2
* ~~Create AWS admin~~
* ~~intigrade with app~~
    * Post/Profile Pictures are uploaded and hosted on AWS now
* ~~See env var problem~~
    * Major security issues with implementation
* ~~Make pictures an upload instead of reference address url~~
* ~~Address database migrations~~
    * Consider adding like property to post

### AWS
The day of reckoning has come and gone. I finnaly got AWS working to host files for the app. As previosly mentoned Heroku will delete all uploaded files after a session has ended. Although this worked for 10mn bursts... we needed a more perminiate solution. AWS solved that problem for us. They now host all of our pictures.

### S3 Buckets
We are using S3 buckets to store our files. This bucket is held on my account and is hosted in US east. Region may play a factor in the reponsiveness of our application. Pictures now load much slower than before at the cost of permanate posts. May want to switch region... not entierly sure. Also for anyone who uses the site plase dont spam large pictures... the bucket does not resize the pic and I will be chagred per gigibate of data uploaded to the server. Have mercy

### AWS Admin
The current admin has given an id key and secret key that acts as a channel for picture uploads to the bucket. If this key is compromised (witch is SUPER likly) given a person a malicous intent.... The key can be closed and a new one can be reinstated. 

### Intigrate with app
I thought this was going to be a pain given how long I've put it off... but it was relitivly easy to intigrate. Litteraly there were 2 packages and a few lines of code and everything was handled! sweet! I was relived how easy this was and I was able to do the whole process in a few hours. Pictures and now uploaded and invoked form the bucket. When you click on a pic this references the server instead of a local file. This happens when hosting localy and vi Heroku.

### ENV veriables
The vulnerabilities of this bucket are caused because we are not using env veriables at this time... We are literaly putting the keys in as string literals and that is extrmely bad practice! In the future we need to set env veriables for django secret key, aws key id, aws secret key... among other things. 

### Upload pics and databse migrations
The website now allows users to upload pics directly. Our modules have been changed from url field to image object. This took a little fenessing to change the database but it ended up working out. A post now consists of an actual pic rather than a url that references a picture hosted elsewhere. Migrations were a success. Furthermore, i experemented with likes... but didnt like my prototype so I scrapted it for now. Likes are easy to set up in the database using a manny to manny relationship... the main issues is its presentability on the page. In my scraped implementation it refreshed the page on like submit... that looked bad and it put the user back at the top of the page. So untill I can figure out a way todo likes without refreshing the page, this feature will be put on the back burnner. However, likes aside the website is 100% funtioning as intended. YAY!

