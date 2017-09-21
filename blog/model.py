#!/usr/bin/python
# -*- coding: utf-8 -*-
#  from flask_login import UserMixin    该类提供了包括is_authenticated()在内的四个flask_login所用方法
from werkzeug.security import generate_password_hash, check_password_hash  # 将密码加密和检查加密后的密码
from app2 import db
from app2 import login_manager
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='users')

    # 该函数是password只有只写属性，如果被读则直接报错
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    # 该函数用于当password被创建时，会被自动set成加密后的password

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    # 该函数用检测password与password_hash的值是否相同

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String)
    body = db.Column(db.String)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def search(value):
        comment = Comment.query.filter_by(id=value).first()
        return comment

'''
# 加载用户的回调函数，
# 一定要定义你必须提供一个 user_loader 回调。
# 这个回调用于从会session存储的用户 ID 重新加载用户对象。
# 它应该接受一个用户的 unicode ID 作为参数，并且返回相应的用户对象。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
'''

