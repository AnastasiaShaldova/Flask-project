from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_required, login_user, LoginManager
from werkzeug.security import check_password_hash

from blog.models.user import Users

__all__ = [
    "login_manager",
    "auth"
]

auth = Blueprint('auth', __name__, static_folder='../static')
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    Users.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template(
            'auth/login.html'
        )

    email = request.form.get('email')
    password = request.form.get('password')
    user = Users.query.filter_by(email=email).one_or_none()

    if not user or not check_password_hash(user.password, password):
        flash('Проверте правильность введенных данных')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"
