from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) # initalizes the Flask app
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS" ] = False

db = SQLAlchemy(app)    