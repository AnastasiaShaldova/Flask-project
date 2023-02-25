from flask import Flask, session

app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return f'Количество посещений на сайте {session.get("visits")}'


@app.route('/del_visit')
def del_visit():
    session.pop('visits', None)
    return 'Данные о посещениях очищены'
