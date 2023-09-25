#from dotenv import dotenv_values

class Config:
    #config = dotenv_values(".env")
    
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    
    """DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']
    DATABASE = config['DATABASE']"""

    user = 'root'
    password = '123456'
    host = '127.0.0.1'
    port = '3306'
    database = 'chat_master'
    
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"