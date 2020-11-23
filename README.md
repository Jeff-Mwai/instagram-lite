# Instagram

#### Author: [Jeff-Mwai](https://github.com/Jeff-Mwai)

## Description
This application is an instagram clone that allows the users to post pictures and captures. It functions almost the same way as instagram, whereby one has to sign up, log in and even update profile.   |

## Behavior Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , you sign up using the registration form| If login is successful, user is navigated to home page | User can comment on the posts that already exists | User is taken to the comment.html page | User comments on the posts |
| Edit profile | On the account link, click on the  update profile | Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Add a new post|Click on the New Profile icon to be redirected to the new post form|the post will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Jeff-Mwai/instagram-lite.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m venv venv
```

```bash
source virtual/bin/activate
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 2.2.8
* Postgresql 
* Boostrap
* HTML
* CSS

## Bugs

* There are no known bugs at the moment

## Support and contact details
 Incase you have any questions or you would like to contribute, kindly reach me through my email at: jeffmwai3@gmail.com

### License

* [[License: MIT]](LICENCE.md) <Jeff-Mwai>               

