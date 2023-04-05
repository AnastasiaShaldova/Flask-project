import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('create-init-user')
def create_init_user():
    from blog.models.user import Users
    from wsgi import app

    with app.app_context():
        db.session.add(
            Users(username='Leo', email='name@example.com', password=generate_password_hash('123456'), is_staff=True)
        )
        db.session.commit()
