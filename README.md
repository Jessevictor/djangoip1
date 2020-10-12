## Gallery
Gallery is a django application that allows users display their photos for others to see.
## Requirements
Clone the the repository by running

```
git clone https://github.com/Jessevictor/djangoip1.git
or download a zip file of the project from github then unzip.
```

Navigate to your project directory

## Create a virtual environment
Install Virtualenv

```
pip install virtual venv
```

To create a virtual environment named virtual, run

```
virtualenv virtual
```
To activate the virtual environment we just created,
run

```
source virtual/bin/activate
```
## Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql

 Then run the following query to create a new database named picsgarage

```
create database gallery
```

## Install dependencies
To install the requirements from requirements.txt file,

```
pip install -r requirements.txt
```

## Create Database migrations
Making migrations on postgres using django
run 

```
python3 manage.py makemigrations garage
```
then run the command below;

```
