from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models.user import Users

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    users = Users.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    users = Users.query.filter_by(id=pk).one_or_none()
    if not users:
        raise NotFound(f"User {pk} doesn't exist!")

    return render_template(
        'users/profile.html',
        users=users,
    )
