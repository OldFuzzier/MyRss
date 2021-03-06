#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from . import main
import os
import sys
out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(out)
import app2  # 注意导入app2与model的先后顺序，一定这么做否则报错 (注意！)
import model
User = model.User
Comment = model.Comment


@main.route('/')
def v_index():
    return render_template('index.html', title="fuzzier's Rss")


@main.route('/about_me')
def v_about_me():
    return render_template('about_me.html')


@main.route('/about_RSS')
def v_about_rss():
    return render_template('about_rss.html')


@main.route('/user_info/<user_id>')
def v_user_info(user_id):
    user_comment_lst = Comment.query.filter_by(user_id=user_id).all()
    user = User.query.filter_by(id=user_id).first()
    return render_template('user_info.html', user_comment_lst=user_comment_lst, user=user)
