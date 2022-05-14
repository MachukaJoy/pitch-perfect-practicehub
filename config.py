from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


# env_path = Path('.')/'.env'
# load_dotenv(dotenv_path=env_path)

class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
class ProdConfig(Config):

  SQLALCHEMY_DATABASE_URI = 'postgresql://bixvunukmlhfvp:7a16d35409378e33ac913ce0a106e50aaaaa39e4b7f76285430da6e8f3574f11@ec2-54-165-184-219.compute-1.amazonaws.com:5432/d9bqgvrnac1iug'

class DevConfig(Config):
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 