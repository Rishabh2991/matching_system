from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = FlaskRedis(app)

from app import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)