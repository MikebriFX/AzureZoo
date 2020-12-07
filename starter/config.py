import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'genesiszoo.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'genesisSQL'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'genesis'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Genes1s1'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blobgenesis'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ufdr4wj3gu+5I6ASfIPy69sy4DxkAz7XNFdXBxADfWd+cGnK7Fb3bybyWghJMNwCbbWzSfoz1b3k5sms6PKkQg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
