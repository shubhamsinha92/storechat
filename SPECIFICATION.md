StoreChat 
Requirements and Specification Document  
*version 1.0*  

# StoreChat

Enter Description here:



## Project Abstract



## Customer


## Competitive Landscape



## User Stories

### Actors:

A single user can be any combination of the following actors:

1. General User - UC Berkeley Student; Access to basic functionality
2. Club Member - N/A for this iteration (UC Berkeley Student that is a member of an organization/club; Access to elevated privileges within scope of club by discretion of club administrator)
3. Club Officer (Administrator) - N/A for this iteration

### User Stories:

#### Iteration 1 User Stories:

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Initial Launch                                                                        |
| Actors:           | General User                                                                          |
| Triggers:         | Access BearClubs URL                                                                  |
| Precondition:     | None                                                                                  |
| Actions:          | Present Sign In//Sign Up Page                                                         |
| Postconditions:   | User now has ability to either sign in or sign up                                     |
| Acceptance Tests: | Assure that "Initial Launch" story only occurs when no user session is stored locally |
| Iteration:        | 1                                                                                     |

| Field             | Description                                                                      |
| ----------------- |:---------------------------------------------------------------------------------|
| Name/Requirement: | Signed In User Launch                                                            |
| Actors:           | General User                                                                     |
| Triggers:         | Access BearClubs URL                                                             |
| Precondition:     | User session stored locally                                                      |
| Actions:          | Present Initial Signed In Page (Profile(?), Directory of Clubs (?), Feed(?))     |
| Postconditions:   | User now has ability to navigate BearClubs with signed in privileges             |
| Acceptance Tests: | Assure that "Signed In User Launch" only occurs when user session stored locally |
| Iteration:        | 1                                                                                |

| Field             | Description                                                                  |
| ----------------- |:-----------------------------------------------------------------------------|
| Name/Requirement: | Sign In                                                                      |
| Actors:           | General User                                                                 |
| Triggers:         | Click Sign In Button                                                         |
| Precondition:     | None                                                                         |
| Actions:          | Present Initial Signed In Page (Profile(?), Directory of Clubs (?), Feed(?)) |
| Postconditions:   | User now has ability to navigate BearClubs with signed in privileges         |
| Acceptance Tests: | Assure that only proper credentials (username, password) allow for sign in   |
| Iteration:        | 1                                                                            |

| Field             | Description                                                                                     |
| ----------------- |:------------------------------------------------------------------------------------------------|
| Name/Requirement: | Sign Up                                                                                         |
| Actors:           | General User                                                                                    |
| Triggers:         | Click Sign Up Button                                                                            |
| Precondition:     | None                                                                                            |
| Actions:          | Present Sign Up Process (Add Clubs (?), Profile Information (?))                                |
| Postconditions:   | User now has an account // User now has ability to navigate BearClubs with signed in privileges |
| Acceptance Tests: | Assure that proper credentials (username, password) allow for sign up                           |
| Iteration:        | 1                                                                                               |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View Directory of Clubs                                                        |
| Actors:           | General User                                                                   |
| Triggers:         | Access Bear Clubs Club Directory URL                                           |
| Precondition:     | None                                                                           |
| Actions:          | Present Club Directory UI                                                      |
| Postconditions:   | User can now view directory of all clubs                                       |
| Acceptance Tests: | Assure that user can navigate to all clubs                                     |
| Iteration:        | 1                                                                              |

| Field             | Description                                                                             |
| ----------------- |:----------------------------------------------------------------------------------------|
| Name/Requirement: | Add Club                                                                                |
| Actors:           | General User                                                                            |
| Triggers:         | Click on Add Club from Directory of Clubs                                               |
| Precondition:     | None                                                                                    |
| Actions:          | Present Add Club dialog                                                                 |
| Postconditions:   | User can now view Club in Club Directory                                                |
| Acceptance Tests: | User can only add a club with proper input // Assure user sees new club on directory    |
| Iteration:        | 1                                                                                       |

#### Iteration 2 User Stories:

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View Club Page                                                                 |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Club in Directory View                                                |
| Precondition:     | User is looking at club directory                                              |
| Actions:          | User views specific club page with prepopulated information                    |
| Postconditions:   | User now learns more about specific club and can navigate back to directory    |
| Acceptance Tests: | Assure that club page is populated with info added when "Adding a Club"        |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                                   |
| ----------------- |:----------------------------------------------------------------------------------------------|
| Name/Requirement: | View User Dashboard                                                                           |
| Actors:           | Logged In User                                                                                |
| Triggers:         | Navigating "home" or various actions that affect user's interactions with clubs, events, etc. |
| Precondition:     | User is signed in and navigates to their subscribed feed of updates                           |
| Actions:          | Redirect user to dashboard and display user subscribed information (updates, calendar, etc.)  |
| Postconditions:   | User can interact directly with subscribed entities (read more about them, view events, etc.) |
| Acceptance Tests: | User dashboard is rendered properly no matter what is subscribed to // User can interact with subscriptions (view events, view clubs, etc.) // Subscriptions can redirect to other entities like club pages       |
| Iteration:        | 2                                                                                             |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View User Profile                                                              |
| Actors:           | Logged In User                                                                 |
| Triggers:         | Click on username from any view                                                |
| Precondition:     | User is signed in and navigates to a certain user's information                |
| Actions:          | Redirect user to profile and display user generated information                |
| Postconditions:   | User can interact directly with other user (invite, email, etc.)               |
| Acceptance Tests: | User profile is rendered properly no matter what informaton provided // User is redirected seamlessly to profile from intial view                                                               |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Add Club Event                                                                 |
| Actors:           | Creator of Club                                                                |
| Triggers:         | None                                                                           |
| Precondition:     | User clicks on add event buton                                                 |
| Actions:          | Present add event dialog                                                       |
| Postconditions:   | User can now see events under events tab                                       |
| Acceptance Tests: | User can only add a event with proper input // Assure user sees new event under events tab |
| Iteration:        | 2                                                                              | 

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Search                                                                         |
| Actors:           | General User                                                                   |
| Triggers:         | Type in search bar                                                             |
| Precondition:     | User clicks on search bar                                                      |
| Actions:          | Present drop down menu with search results                                     |
| Postconditions:   | User can see results for a search query                                        |
| Acceptance Tests: | User will see results related to search query // Assure user can't see search results they don't have pemissions for  |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Join Club                                                                      |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Join Club button on Club Page                                         |
| Precondition:     | User is signed in and not already a member of the club                         |
| Actions:          | Present form for user to fill out (?)                                          |
| Postconditions:   | User can see the club listed in their profile // User is now a member of the club and has certain member privileges/permissions                                 |
| Acceptance Tests: | User can only join if the form is filled out correctly and is approved         |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Promote Member to Admin                                                                     |
| Actors:           | Existing organization admin (default organization creator)                                                                  |
| Triggers:         | Button on club profile page                                         |
| Precondition:     | User is signed in and is an admin of the organization                         |
| Actions:          | Select members to promote; confirm button                                          |
| Postconditions:   | Member promoted is now admin                             |
| Acceptance Tests: | Members promoted has full admin priviledges (create events for now)       |
| Iteration:        | 2                                                                              |


### User Stories For Future Iterations:



## User Interface Requirements

![UI Requirements]
