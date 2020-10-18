from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'username@example.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = 'username@example.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{databasename}".format(
username = "flask_user",
password = "flask_user",
hostname = "34.84.115.147",
port = 3306,
databasename = "livetracking",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mySecretKey'
db=SQLAlchemy(app)
ma = Marshmallow(app)


from Backend import route
