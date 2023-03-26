from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    is_staff = Column(Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, is_staff):
        self.username = username
        self.email = email
        self.password = password
        self.is_staff = is_staff

