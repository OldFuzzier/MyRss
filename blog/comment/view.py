#!/usr/bin/python
# -*- coding: utf-8 -*-

from .import comment
from flask import request, render_template, redirect, url_for, render_template_string, session
import os
import sys
from form import CommentForm
#导入上级目录的文件
out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(out)
import app2, model
db = app2.db
User = model.User
Comment = model.Comment


@comment.route('/post', methods=['POST', 'GET'])
def v_post():
    form = CommentForm()
    if request.method == 'POST':
        c = Comment(theme=form.theme.data, body=form.body.data, user_id=session['user_id'])
        db.session.add(c)
        db.session.commit()
        return redirect('/')
    return render_template('comment.html', form=form)


# @login_required 检查用户是否登录
@comment.route('/edit/<int:uid>', methods=['POST', 'GET'])
def v_edit(uid):
    post = User.search(uid)
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', title='Edit', post=post)
