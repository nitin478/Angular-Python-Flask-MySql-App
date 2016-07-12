# Angular-Python-Flask-MySql-App

# Setup:
## Unix (default Python 2.7), Copy & pastable commands:

#####sudo apt-get update
#####sudo apt-get git
#####sudo apt-get -qq -y install python-pip python-mysqldb
#####git clone https://github.com/nitin478/Angular-Python-Flask-MySql-App.git
#####cd Angular-Python-Flask-MySql-App
#####sudo pip install -r requirements.txt


# Run Application:

### Add DB configurations in config.py.

Sample:

    class SQLConfig:
        USER_ID = <db_user>
        PASSWORD = <db_user's_password>
        IP = <db_ip>
        DB = <database_name>

### Run command:

    python webapp.py

### Use Instance's external IP to access the application in web browser.

    http:<instance_ip>:8000/


