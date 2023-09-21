#from dotenv import dotenv_values

class Config:
    #config = dotenv_values(".env")
    
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    
    """DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']"""

    #Para probar
    host = "127.0.0.1"
    user='root'
    port = "3306"
    password='123456'
    
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"