#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
该模块功能类似于flask_login
'''
from flask import url_for, session, request


class LoginManager(object):
    def __init__(self):
        self.login_view = None


def login_user(user):
    session['user_id'] = user.id
    session['user_name'] = user.username
    return True


def logout_user():
    if 'user_id' in session:
        session.pop('user_id')
    return True


def login_required(func):
    def decorated_view(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return url_for('auth.v_login')
    return decorated_view
