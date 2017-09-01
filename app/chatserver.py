from flask import Flask
from extensions import mongo
import view.viewmodule

def create_server():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    configure_extensions(app)
    configure_blueprints(app)

    return app

def configure_extensions(app):
    mongo.init_app(app)

def configure_blueprints(app):
    app.register_blueprint(view.viewmodule.views)
