from flask import Flask, redirect, url_for
from flask_login import LoginManager

from blog.auth.views import auth
from blog.articles.views import articles
from blog.models.database import db
from blog.models.user import Users
from blog.user.views import user
from blog.visit.views import visits

__all__ = [
    "login_manager",
    "create_app"
]

login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "52(%iw-2y)t0vluomb8u^h22dd*qpl81ut^2ytp(djd^1#w61_"
    db.init_app(app)
    register_blueprints(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        Users.query.get(int(user_id))

    # @login_manager.unauthorized_handler
    # def unauthorized():
    #     return redirect(url_for('auth.login'))

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles)
    app.register_blueprint(visits)
    app.register_blueprint(auth)

