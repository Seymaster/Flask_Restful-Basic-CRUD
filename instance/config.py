import os
import datetime


DEBUG = True

# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://seymaster512:London009@db4free.net:3306/hspbookings'
SQLACHEMY_TRACK_MODIFICATIONS = True


# Mail configurations
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True 
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = "squadbytevoluteers@gmail.com"
MAIL_USERNAME = "squadbytevoluteers@gmail.com"
MAIL_PASSWORD = "English2018"


#  locally database configuration
# SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/service1'
# SQLACHEMY_TRACK_MODIFICATIONS = False

# Support email
sup_email = "alugbinoluwaseyi1@gmail.com"