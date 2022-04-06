from flask import Flask
from os import path
#from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "HelloWorld"
        
    #relitive import / import a file inside of the python package.
    from .views import views
    #from .auth import auth
    
    #register the blue prints
    app.register_blueprint(views, url_pefix="/")
    #app.register_blueprint(auth, url_pefix="/")
    
    return app