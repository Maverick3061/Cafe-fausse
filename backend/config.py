import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Talha%403061@localhost:3306/cafe_fausse"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dev-key"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your_email@gmail.com"
    MAIL_PASSWORD = "your_app_password"
