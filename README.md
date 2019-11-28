# DEMS

Dems is a python based web app to provide easy checkin and checkout facilities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
pip install django
pip install requests
pip install virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running in a virtual environment.
First move to some directory and run these commands.

```
git clone 
```
![alt text](https://github.com/SDISON/Dems/blob/master/img/01.png)
```
virtualenv venv
```
![alt text](http://url/to/img.png)
```
source venv/bin/activate
```
![alt text](http://url/to/img.png)
```
cd dems
python manage.py migrate
```
![alt text](http://url/to/img.png)
```
python manage.py makemigrations login
python manage.py migrate login
python manage.py makemigrations logout
python manage.py migrate logout
```

### Before running server provide these to run messaging service in webapp.
1.Open send_mail.py file from dems/login/ and change username and password to you gmail account and password.
2.Open send_mail.py file from dems/logout/ and change username and password to you gmail account and password.
3.Create account on way2sms for sending messages on phone.
4.Open sms.py file from dems/login/ and provide your apikey,secretkey,and phone number with which you registered.
5.Open sms.py file from dems/logout/ and provide your apikey,secretkey,and phone number with which you registered.

And run this command to run django server

```
python manage.py runserver
```
![alt text](http://url/to/img.png)

For checking details regrading your table view admin page(127.0.0.1/admin).

To make admin account follow these steps and enter valid credentials.

```
python manage.py createsuperuser
```

![alt text](http://url/to/img.png)


## Built With

* [Django](https://www.djangoproject.com/) - The web python framework used
 

## Authors

* **SUSHEN SHROTRIYA** - Student


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

