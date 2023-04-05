from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm
from blog.models.user import Users

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if Users.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not unique')
            return render_template('users/register.html', form=form)

        _user = Users(
            email=form.email.data,
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )

        db.session.add(_user)
        db.session.commit()
        login_user(_user)

        return render_template(
            'users/register.html',
            form=form,
            errors=errors
        )


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
