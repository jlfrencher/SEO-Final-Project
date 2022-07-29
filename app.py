from flask import Flask
from extensions import *
from config import SECRET_KEY
import main
import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    register_extensions(app)
    register_blueprints(app)

    from models import User

    with app.app_context():
        db.create_all()

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

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")