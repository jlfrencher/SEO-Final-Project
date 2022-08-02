from flask import Flask
from extensions import *
from config import SECRET_KEY
import logging
import main
import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    register_extensions(app)
    register_blueprints(app)

    from models import User, Slot

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(e)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

def register_extensions(app):
    db.init_app(app)
    proxy.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    app.register_blueprint(main.main)
    app.register_blueprint(auth.auth)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")