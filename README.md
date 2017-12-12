# Restful Web Application

Build backend REST API using Django Rest Framework.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Setting Up Your Virtual Environment
The first thing we'll do as part of our application is to set up the virtual environment. Enter the following commands in your Terminal:

`conda create --name myEnv`
`activate myEnv`

### Installing the Django Application
Inside the projects folder, install the necessary requirements
`pip install -r reuirements.txt`

## Running the Application
### Switch to project location
`cd src/webapp_project`

### Apply the schema migration
Migrations are Django’s way of propagating changes you make to your models (like adding a field, deleting a model, etc.)
into your database schema. Now that we have a rich model in place, we need to tell the database to create the relevant schema.
In your console, run this:
`python manage.py migrate`

### Run Server
We'll run our server the django way with the runserver command:
`python manage.py runserver`

Enter the server specified URL (http://127.0.0.1:8000/api) in your browser.
