from flask import Flask

from blog.articles.views import articles
from blog.user.views import user
from blog.visit.views import visits


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(articles)
    app.register_blueprint(visits)
