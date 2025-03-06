from flask import Flask
from .extensions import db
from .controllers.campaign import campaign_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(campaign_bp)

    # Create DB tables if they don't exist
    with app.app_context():
        db.create_all()

    return app