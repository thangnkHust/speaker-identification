from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from .models import db

from .controllers import Hello, TodoList, Todo

def create_app(flask_env = 'dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[flask_env])

    api = Api(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    CORS(app)

    api.add_resource(Hello, '/')
    api.add_resource(TodoList, '/todo/')
    api.add_resource(Todo, '/todo/<id>')

    return app
