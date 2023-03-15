from flask import Blueprint, session, render_template


visits = Blueprint('visits', __name__, url_prefix='/', static_folder='../static')


@visits.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template('visit/list.html', visits=session.get("visits"))


@visits.route('/del_visit', methods=['DELETE'])
def del_visit():
    session.pop('visits', None)
    return render_template('visit/list.html')
