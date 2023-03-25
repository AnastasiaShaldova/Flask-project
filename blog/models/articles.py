from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean

from blog.models.database import db


class Articles(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    text = Column(String)
    # author = relationship('Users.id')
