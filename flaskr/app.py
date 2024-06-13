import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


STATIC_DIR = os.path.abspath('/media/khoa/Download/URLShortener/flaskr/static')


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = 'ad23b7a4-d683-4a4d-b340-77c7b89a7529'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@localhost:3306/URL_shortener"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'khoatm20@gmail.com'
app.config['MAIL_PASSWORD'] = 'qloj wxqc xbdy vrgl'
mail = Mail(app)
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
from flaskr.routes.homepage import homepage
from flaskr.routes.user_management import user_management
from flaskr.routes.link_management import link_management
from flaskr.routes.login import login
from flaskr.routes.register import register
from flaskr.routes.redirect_short_link import redirect_short_link
from flaskr.routes.user import user_blueprint
from flaskr.routes.link import link_blueprint
from flaskr.routes.mail import mail_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(link_blueprint)
app.register_blueprint(mail_blueprint)