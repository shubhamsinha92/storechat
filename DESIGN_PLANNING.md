StoreChat 
Design and Planning Document  
*version 1.0*  

# StoreChat

Description Here:



## System Architecture

### Client-Server Overview

We will be creating a client-server web application. We will follow a Model-View-Controller (MVC) pattern, using HTML5/JavaScript for the client and Django for the server side. The key components in this system will be:

* Database: We will store relevant raw data/information about our users, organizations, and events in a database.

* Backend Server: The server will be implemented in Django. It will access the database for raw data and communicate with the client for sending and receiving data requests/responses.

* Frontend Web Client: We will implement the client using HTML5/CSS to display information and JavaScript to transfer and parse data to and from the server as needed.

### MVC/MTV Overview


* Model: This describes the database tables, allowing us to create, retrieve, update, and delete records about our users, organizations, and events. The model will also provide the business logic, manipulation of data to carry out functionalities needed for the application.

* Template: This is the part that creates what the user actually sees when using the application. We use HTML5/CSS to create templates and determine what data to display and how to display it. We use JavaScript to request data that needs to be displayed.

* View: This deals with data requests from the client side and returns appropriate responses. It renders data for the templates that will be displayed in the web client.

## Design Details

The following sections in Design Details are under active development; they will be subject to change during the first two iterations while we dial in our datastructures, etc.

### Frontend App Details



### Backend Server Details

Our backend will be written in Web2py. The server will process incoming requests and manage access to the global database, as well as build and serve pages and manage password encryption and authentication. There are many Django packages that can help us manage these tasks. Since our application is targeted for UC Berkeley students, we are also considering running our user registration and authentication system through CalNet in a later iteration.

### Database Details

We will be using SQLite for local development, and PostgreSQL on production. We chose local SQLite for speed of development and ease of use, and production PostgreSQL for scale and performance. Our database will store users and their related profile information, organizations and their related profile information, events and their relevant information, as well as provide mappings between these three main models:  

Users: username, email, first name, last name  
Organization: name, description, location, contact info, type  
Event: name, description, start time, end time, location  

We will also have mapping / relational tables to link our users to organizations and events to organizations; a rudimentary diagram is shown below, and will be updated with future iterations.

##### Data Tables

*All tables have a `UNIQUE PRIMARY KEY` field of type integer with name `id`*

###### USER

| Field             | Description                            |
| ----------------- |:---------------------------------------|
| username          | required unique char(128)              |
| email             | required unique char(128)              |
| first\_name       | required char(128)                     |
| last\_name        | required char(128)                     |

###### ORGANIZATION

| Field             | Description                       |
| ----------------- |:----------------------------------|
| name              | required char(128)                |
| description       | required textblob                 |
| location          | char(128)                         |
| location_lat      | double                            |
| location_long     | double                            |
| contact\_info     | char(128)                         |
| type              | required foreign key org_type(id) |

###### ORGANIZATION_TYPE

| Field             | Description                       |
| ----------------- |:----------------------------------|
| name              | required char(128)                |
| description       | required textblob                 |


##### Mappings / Relations

###### User to Organization

| Field                | Description                            |
| -------------------- |:---------------------------------------|
| fk\_user\_id         | required foreign key user(id)          |
| fk\_organization\_id | required foreign key organization(id)  |
| admin                | required bool                          |
| position             | char(128)                              |


#### Invariants

* User
    * Must have valid username.
    * Must have valid email.
    * Must have valid first name and last name.
    * Must be associated with zero or more organizations (user to organization mapping).
* Organization
    * Must be associated with at least one admin member.
    * Must be associated with at least one member.
    * Must have valid name.
    * Must have valid contact info.
* Event
    * Must have valid name.
    * Must have start time and end time (start time must be before end time).
    * Must be associated with exactly one club.

#### Algorithms



#### Protocols


#### View/Template Details

Views in Django are similar to how controllers function in a traditional MVC design pattern. Our views will act as the glue between our models and templates; passing data objects to our templates for rendering, accepting `POST` data for processing, and so on.

In iteration 1, we'll be solidifying our overall UI style guide, but common themes will persist through the application:

* Main layout
    * Header across the top of all pages of the application
        * Navigation links (left floating)
            * BearClubs (home)
            * Clubs (clubs directory)
            * Discover (directory search page)
        * User links (right floating)
            * My Profile (user memberships, settings, etc.)
            * My Calendar (upcoming events, subscribed events)
            * My Clubs (list of user's clubs)
    * User Sidebar (floating left, entire height of content area)
        * Profile picture
        * Username
        * Full name
        * Small version of calendar (upcoming week of events)
    * Content area
        * Main content will be rendered here (yield to other views)
* Sign up / Sign in layout
    * Header (same as main layout)
    * No Sidebar (user isn't signed in / registered yet)
    * Content area
        * Centered form / modal dialog
            * Register (left half of div)
                * Username field
                * Email field
                * Confirm email field
                * Password field
                * Confirm password field
                * Register button
            * Sign in (right half of div)
                * Username or Email field
                * Password field
                * Sign In button
                * Forgot username / password button
* Club Directory
    * Header (same as main layout)
    * Sidebar (same as main layout)
    * Content area
        * Sub-header (across top of content area)
            * Live updating search bar
            * Filter options (items per page, A-Z search, etc.)
        * Directory view
            * Live updating list of organizations
            * Table view
                * Each row clickable; directs to club's profile
* Club Profile
    * Header (same as main layout)
    * Sidebar (same as main layout)
    * Content area
        * Sub-header (across top of content area)
            * Cover photo
            * Name of organization
            * Next meeting
        * Profile information
            * Sidebar (right floating)
                * Subscribe button (get notified of updates / add events to calendar)
                * Officer information
                * Contact information
                * Location (offices)
                * Upcoming events
            * Main content
                * News feed of updates, events, etc.

#### Class Descriptions

Iteration 1 only describes two major class implementations initially; `User` and `Organization`

* User :: User model for interacting with user objects
    * Accessor methods; `getUserID()`, `getUsername()`, `getClubs()`, etc.
    * Authentication methods; `loginUser(id, pass\_hash)`, `getAdminRights()`, etc.
    * More complex methods like getClubs() will interact with mappings (user-club-mapping, etc.)
* Organization :: Model implementation for organization objects
    * Accessor methods; `getUsers(admin_level)`, `getAdmins()`, `getOfficers()`, `getOrgName()`, etc.
    * Authentication methods; `getUserAuthLevel(user_id)`, `grantUserAdmin(user_id`, etc.
    * Authentication methods will be limited to entities with admin rights for each organization to prevent members from promoting themselves, demoting others, and other sensitive operations (future iterations)

## Implementation Plan

### Iteration 1


### Iteration 2



##### Entire StoreChat Team Tasks (These will happen before the start of tasks by any team)

##### Interface Design Team

* Number of Days to Develop: 8
* Number of Days to Test: 2

###### Sub-tasks


