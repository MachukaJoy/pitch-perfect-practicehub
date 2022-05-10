import os



class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:superuser@localhost/pitchdb'
  # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  print(SQLALCHEMY_DATABASE_URI)
  Debug=True