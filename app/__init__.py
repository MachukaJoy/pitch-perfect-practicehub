from flask import Flask
from config import Config
app = Flask(__name__)

def create_app():
    app.config.from_object(Config)
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    return app 