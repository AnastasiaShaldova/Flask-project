from flask import Blueprint, render_template
from flask_login import login_required

from blog.models import Users

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
    _users = Users.query.filter_by(id=pk).one_or_none()
    if not _users:
        return f'Not found {pk}'
    return render_template(
        'users/profile.html',
        users=_users,
    )
