import os
DEBUG = True

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '010125'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'SPS'
SECRET_KEY = os. environ. get( 'SECRET_ KEY') or 'you will never guess'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True