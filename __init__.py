from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'idontknowwhatimdoingimjustlearning'

    from .view import view
    from .auth import auth

    app.register_blueprint(view, url_prefix='/view')
    app.register_blueprint(auth, url_prefix='/auth')
    
    return app