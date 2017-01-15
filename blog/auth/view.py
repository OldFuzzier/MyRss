#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from flask import render_template, request, redirect, url_for, flash, session
from . import auth
from form import LoginForm, RegistrationForm
out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(out)
from my_login import login_user, logout_user, login_required
#from flask_login import login_required
import app2, model
db = app2.db
login_manager = app2.login_manager
User = model.User


@auth.route('/login', methods=['GET', 'POST'])
def v_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)  # 相当于记住session
            return redirect(url_for('main.v_index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
def v_logout():
    if 'user_id' in session:
        logout_user()  # 删除session，用于用户登出
        flash('You have been logged out')
        return redirect(url_for('main.v_index'))
    else:
        return render_template('auth/auth_404.html'), 404


@auth.route('/register', methods=['GET', 'POST'])
def v_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now Login')
        return redirect(url_for('auth.v_login'))
    return render_template('auth/register.html', form=form)

