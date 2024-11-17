
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")
app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
#en saanut toimimaan. Koita korvata getenv("DATABASE_URL") serverin linkillä
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)