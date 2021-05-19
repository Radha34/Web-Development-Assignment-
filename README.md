WEB DEVELOPMENT ASSIGNMENT

Library Management System 

Clone the git repository and setup the project.
Change the DATABASE_URL value to your database url, also change value of your secret key.

Project Pre-requisites & Dependencies: python3.x postgresql pipenv

flask flask sqlalchemy psycopg2 flask-migrate flask-script flask-bcrypt pyjwt manage requests

pip install pipenv pipenv shell pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script flask-bcrypt pyjwt manage

Run the following from your terminal (if windows, if linux change SET for $ export) SET PORT=5432 SET FLASK_ENV=development SET DATABASE_URI=postgres://postgres:radha@localhost:5432/library 

Run the command python app.py 
