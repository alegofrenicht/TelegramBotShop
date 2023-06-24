from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv

app = Flask(__name__)
app.config['DEBUG'] = True
SQLALCHEMY_DATABASE_URI = getenv('DB_URI')
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Microlab2gavno9@localhost/random_database"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, bot