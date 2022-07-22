# from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)

DB_URL = 'postgresql+psycopg2://postgres:123456@localhost/mydb'

#'postgresql://postgres:123456@localhost:5432/mydb'
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)
migrate = Migrate(app, db) # this
