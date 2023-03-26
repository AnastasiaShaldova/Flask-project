from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.database import db

app = create_app()

app.run(
    host="0.0.0.0",
    debug=True,
)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("БД создана")

@app.cli.command("create-users")
def create_users():
    from blog.models import Users
    admin = Users(username="admin", email="admin@admin.ru", password=generate_password_hash('123456'),  is_staff=True)
    james = Users(username="james", email="james@james.ru", password=generate_password_hash('123456'), is_staff=False)
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("Созданные пользователи: ", admin, james)
