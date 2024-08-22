from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask_backend'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database and migration tool
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from home.routes import home_bp
    from shorten_urls.routes import shorten_urls_bp
    from pastelockly.routes import pastelockly_bp
    from scrappy.routes import scrappy_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(shorten_urls_bp, url_prefix='/shorten_url')
    app.register_blueprint(pastelockly_bp, url_prefix='/pastelockly')
    app.register_blueprint(scrappy_bp, url_prefix='/scrappy')

    return app
