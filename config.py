import os



class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:superuser@localhost/pitchdb'
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY=os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  Debug=True