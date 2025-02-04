from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints or routes
    from app.controllers.deepseek_controller import deepseek_bp
    app.register_blueprint(deepseek_bp)
    # ..
    return app