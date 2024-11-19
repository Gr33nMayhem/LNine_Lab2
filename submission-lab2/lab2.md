# Results for Lab 2

This is the submission for Lab 2. The results are depicted as screenshots along with the instructions as to how these can be replicated.

## Task 1: Authentication
The project has an authentication application which handles all the authentication related tasks. The user can sign up, log in, log out, and reset password. The user can also update their profile information.

Fig 1. This is the screenshot of the admmin page with information about the models used. The models are: CustomUser, UserProfile, and Company

![admin](https://github.com/user-attachments/assets/edc12903-4deb-48c9-ad46-01a73a1b7119)

Fig 2. This is the screenshot of the home page. Here the links in the side menu to the left are not linked and will not work. On the top right of the screen We see the "Log In" button to open the login page.

![home](https://github.com/user-attachments/assets/c8c9aaf4-fe49-4d6c-97a8-e326ab9357f7)

Fig 3. This is the screenshot of the login page. Here the user can enter their username and password to log in. The user can also click on the "Forgot Password" link to reset their password.

![login](https://github.com/user-attachments/assets/f674dc3e-440b-4a41-8811-ac04599c4571)

Fig 4. This is the screenshot of the sign up page. Here the user can enter their details to sign up. The user can also click on the "Log In" link to go to the login page.

![signup](https://github.com/user-attachments/assets/149dece0-b128-4c1e-9579-f39de999fdc8)

Fig 5. This is the screenshot of the reset password page. Here the user can enter their email address to reset their password. The user can also click on the "Log In" link to go to the login page.

![reset_pass](https://github.com/user-attachments/assets/5f4f78ce-0baa-4329-bc4c-23b566c58e6a)

Fig 6. Once again this is the screenshot of the home page, here you can see that when a user is logged in, they can switch between User Profiles or Create a new User Profile.

![home_loggedin](https://github.com/user-attachments/assets/0638611f-3de4-49c9-a7d7-c859e4ed535c)

Fig 7. This is the form that opens when the user tries to create a new User Profile, using the link in the previous screen shot.

![create_profile](https://github.com/user-attachments/assets/bab097b3-dc4b-4813-b46d-204d69682a06)

## Task 2: Localisation
These screenshots explain how the languages can be changed.

Fig 8. This is the screenshot of the home page. Here the user can see the language dropdown on the top right where the flag of the language is displayed. The user can then pick from the dropdown which language they wish to change to.

![translatedt to spanish](https://github.com/user-attachments/assets/0505f55c-fdbf-4cff-bce8-04d6e60a6a69)


![spanish 2](https://github.com/user-attachments/assets/dfad97ba-3051-4105-9dce-2370beaa615e)


## Installation Instructions

### Installation
1. Clone the repository

```bash
$ git clone <url>
```

2. Install the requirements.txt

```bash
$ pip install -r requirements.txt
```

3. Run the server and test

```bash
$ python manage.py runserver
```

## Instructions for the evaluator
NOTE: Please make sure to add the static/ provided with the project to see proper styling. The static folder should be placed under the BASE_DIR of the project.
NOTE: The project comes with fixtures. The seed user is system and the email is system@example.com. The password is System123_ and the user is a superuser. The company is also seeded with the name "HelloWorld Company". To load the fixtures run the following commands:
```bash
$ python manage.py loaddata accounts/fixtures/user.json
$ python manage.py loaddata accounts/fixtures/company.json
```
NOTE: Make sure to use the email to login and not the username.

