# Results for Lab 2

This is the submission for Lab 2. The results are depicted as screenshots along with the instructions as to how these can be replicated.

## Task 1: Authentication
The project has an authentication application which handles all the authentication related tasks. The user can sign up, log in, log out, and reset password. The user can also update their profile information.

Fig 1. This is the screenshot of the admmin page with information about the models used. The models are: CustomUser, UserProfile, and Company

Fig 2. This is the screenshot of the home page. Here the links in the side menu to the left are not linked and will not work. On the top right of the screen We see the "Log In" button to open the login page.

Fig 3. This is the screenshot of the login page. Here the user can enter their username and password to log in. The user can also click on the "Forgot Password" link to reset their password.

Fig 4. This is the screenshot of the sign up page. Here the user can enter their details to sign up. The user can also click on the "Log In" link to go to the login page.

Fig 5. This is the screenshot of the reset password page. Here the user can enter their email address to reset their password. The user can also click on the "Log In" link to go to the login page.

Fig 6. Once again this is the screenshot of the home page, here you can see that when a user is logged in, they can switch between User Profiles or Create a new User Profile.

Fig 7. This is the form that opens when the user tries to create a new User Profile, using the link in the previous screen shot.


## Task 2: Localisation
These screenshots explain how the languages can be changed.

Fig 8. This is the screenshot of the home page. Here the user can see the language dropdown on the top right where the flag of the language is displayed. The user can then pick from the dropdown which language they wish to change to.

## Installation Instructions

### Installation
1. Clone the repository

'''bash
$ git clone <url>
'''

2. Install the requirements.txt

'''bash
$ pip install -r requirements.txt
'''

3. Run the server and test

'''bash
$ python manage.py runserver
'''

## Instructions for the evaluator
NOTE: Please make sure to add the static/ provided with the project to see proper styling. The static folder should be placed under the BASE_DIR of the project.
NOTE: The project comes with fixtures. The seed user is system and the email is system@example.com. The password is System123_ and the user is a superuser. The company is also seeded with the name "HelloWorld Company". To load the fixtures run the following commands:
'''bash
$ python manage.py loaddata accounts/fixtures/user.json
$ python manage.py loaddata accounts/fixtures/company.json
'''
NOTE: Make sure to use the email to login and not the username.

