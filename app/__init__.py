from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()



def create_app():

    app = Flask(__name__)   
    app.config.from_object(Config)


    #register packages
    login_manager.init_app(app)
    db.init_app(app)              #replaced by SQLAlchemy(app) above [huh???]
    migrate.init_app(app, db)     

    #import blueprints


    #register blueprints

    return app






from app import routes, models

