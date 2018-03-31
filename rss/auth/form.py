#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError  #报错时使用
out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(out)
import model
User = model.User


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    #  remeber_me = BooleanField('Keep me Logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp(
            regex='^[A-Za-z][A-Za-z0-9_]*$', message='username must have only letters, numbers,etc')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    #  以validate_开头的函数且后面跟着字段名(比如username),这个方法会和常规验证函数一起调用
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
