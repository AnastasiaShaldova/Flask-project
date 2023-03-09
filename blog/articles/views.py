from flask import Blueprint, render_template, redirect, url_for
from werkzeug.exceptions import NotFound

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


ARTICLES = {
    1: {
        'title': 'Символы Юникода',
        'text': 'Добавлять юникод-символы в строковые литералы можно не только с помощью их номеров, но и по их названиям.',
        'author': 1
    },
    2: {
        'title': 'Функция zip',
        'text': 'Функция zip создаёт итератор, который комбинирует элементы нескольких списков. Это позволяет осуществлять параллельный обход списков в циклах for или, например, выполнять параллельную сортировку.',
        'author': 2
        },
    3: {
        'title': 'Проверка отношения классов',
        'text': 'Для того, чтобы проверить отношения двух классов или экземпляров (является ли класс классом наследником), есть две простые встроенные функции isinstance(object, classinfo) и issubclass(class, classinfo). instance - возвращает True, если объект является экземпляром класса либо экземпляром подкласса данного класса. issubclass — проверяет является ли класс наследником другого класса. Данные функции зачастую применяются в ООП.',
        'author': 3
        },
}


@articles.route('/')
def articles_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@articles.route('/<int:pk>')
def get_articles(pk: int):
    try:
        articles_id = ARTICLES[pk]
        articles_title = ARTICLES[pk]['title']
        articles_text = ARTICLES[pk]['text']
        articles_author = ARTICLES[pk]['author']
    except KeyError:
        raise NotFound(f'Articles id {pk} not found')
    return render_template(
        'articles/details.html',
        articles_id=articles_id,
        articles_title=articles_title,
        articles_text=articles_text,
        articles_author=articles_author
    )
