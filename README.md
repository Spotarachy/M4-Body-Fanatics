![CI logo](/media/My%20logo/IMG_8940.jpg)

Welcome Body Fanatics
**,June 20 2022**

### Introduction

This website was made as the name's suggests for real fanatics when it comes to physical fitness, endurance, and over-all passion for Health, we listen to the advice & opinions of the fitness industry & we believe that we have created a strong Community to have everything you need in one place, come on jones.

## Table of Content

1.[UX - User Experience](#ux) 

  * [Project Goals](#project-goals)
    * [MVC framework](#MVC-framework)
    * [Authentication](#authentication)
    * [E-commerce](#e-commerce)
    * [Control-system](#control-system)


  * [User Stories](#user-stories)
    * [Database schema](#database-schema)
    * [Functionality](#functionality)
        
        .[Create](#create)
        .[Read](#read)
        .[Update](#update)
        .[Delete](#delete)


2.[Design](#design)

  * [colour](#colour)
    
  * [Typography](#typography)

  * [Images](#images)
    * [Pexels.com](#Pexels)
    * [AliExpress.com](#aliExpress)
    * [Storenvy.com](#storenvy.com)
    * [VectorStock.com](#font-awesome)

  * [Icons](#icons)
    * [Font Awesome ](#font-awesome)
    * [Bootstrap](#bootstrap)

  * [Layout](#layout)

  * [Wire frames](#wire-frames)

3.[Features](#features)

  * [Validator](#validator)
     * [HTML-VAL](#val)
     * [CSS-VAL](#val)

  * [Testing](#Testing)
  
  * [Bugs](#Bugs)

4.[Data](#data)

  * [Application](#application)
    * [CRUD](#crud)
    * [CodeBase](#codebase)
    * [TDD Approach](#tdd)
    * [Template Django](#template)
    * [Schema](#schema)
    * [Version control](#version)

5.[Developmnet](#Developmnet)

    * Horoku

    * Github

    * Mongo DB

   * [Credit](#Credit)
   * [Acknowledgements](#Acknowledgement)





# UX - User experience

We want to give her use of the place where they can come and feel comfortable, here and `Body Fanatics` we aim to have easily viewed purchases in shopping cart to avoid overspending

Give them a place where easily register in their account or login or recover their passwords, in case they forget it 
We aim to have a fully functional in store that receive emails and confirmations of the registration of their account,
And make sure each user has a personalise profile within them cells can become a seller on our website.


---


## MVC framework

![Mockup](/media/framework/Screenshot%202022-03-23%20at%204.11.53%20PM.png)

### Mobile app

This is an example of the email and password and login page on the mobile app easily downloaded and accessible when will available


### Layout of website

![Mockup](/media/framework/Screenshot%202022-03-23%20at%204.39.40%20PM.png)


From the layout of the website shoppers will be easily views of the list of products as individual products & thire details, these are quickly identified and items specified, and offers are clearly sense of direction through a drop-down menu for ease of use.


---

## Authentication
This will be done into steps to differentiate our customers between our sellers will be able to add their own products and sign users will be able to shop are parts,

### Superusers

* As a superuser you'll be able to edit add or delete items from the store and become a seller of your own products on the body fanatics website this is done with the admin on location of the shop was super users can be registered by our team, they will have full control to edit there products add new items to the shop or change the existing items such as prices, description, images, or update to existing product.


### Side uses 

* excite user can easily register for an account easy login easily recover their passwords in case of misuse and have a personalise use a page where there they can see a list of there pass purchases,


---


## E-commerce

This section of the store will be handled by '''stripe''' payment system and link to our e-commerce store here customers will be able to check out and make purchases directly from their account, 
It will be handled in the background, customers will receive confirmation emails with shipping and handling details, for each specific products and information from their past purchases will be displayed and also if they qualify for any discounts in shipping.


---

## Control-system

Using '''Heroku''' will be able to log in and check how the site is doing to the backend of the site will be able to monitor as a super admin user can use the website admin to make sure the website is running smoothly,

You'll be able to monitor the push notification  of are users are that are registered to the admin and simultaneously get all the account details that are stored.

Well we can monitor if a customer as a new product or delete a current product this all will be registered to the terminal which again will be pushed to our server at Heroku


---

# User Stories

* first visit: Have a very eye appealing look the first time users easily navigated all the information is clearly displayed and very customisable to their preferences with this we hope to have a first time user register for an account, and become a customer

~~~
    * How fast is the website loading.
    * Is the website easy to understand.
    * Does it have quick responses.
    * How's the design.
    * All the links should work.
    * Easy to navigate.
    * Not confusing.
    * Simple. 
    * Interactive.

~~~

* Returning visitor: have a personal account and be able to view my profile be able to access my personal account information, easily required  access to my account, verified my account system is working and securely stored in my past orders and change my address or payment system if I want to I need to.

~~~
* can I see my shopping bag
* can I increase the amount of my purchase
* is there a different sizes available
* can I find different trainers
* deals or discount
* is there a new arrivals
* can I can I join a group lesson
~~~

These are some of the user experiences and stories we would like to fulfil for customers here `body fanatics`


---
















## How to Deploy 

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.


1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked


------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.



```
pkill uptime.sh
rm .vscode/uptime.sh
```
---

'''
Thank you CodeInstitute for helping me become more than who I was meant to be.
'''

- [ ] Mario F Wilson :tada:
