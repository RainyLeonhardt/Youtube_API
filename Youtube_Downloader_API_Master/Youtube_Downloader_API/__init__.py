# Import the necessary tools
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new SQLAlchemy object
db = SQLAlchemy()
# A variable to store the name of the database
YOUTUBE_DATABASE = "youtube_database.db"

def create_web_app():
    # Create a Flask object called app
    app = Flask(__name__)

    # Set up the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{YOUTUBE_DATABASE}'
    db.init_app(app)

    # Register the blueprint
    from .home import home
    app.register_blueprint(home, url_prefix='/')

    # Create the database
    with app.app_context():
        db.create_all()

    # When create_web_app is called elsewhere, return the app object to the caller
    return app