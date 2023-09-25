from dotenv import dotenv_values

class Config:
    config = dotenv_values(".env")
    
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    
    user = config['DATABASE_USERNAME']
    password = config['DATABASE_PASSWORD']
    host = config['DATABASE_HOST']
    port = config['DATABASE_PORT']
    database = config['DATABASE_NAME']


    """Para probar
    host = "127.0.0.1"
    user='root'
    port = "3306"
    password='123456'"""
    
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"