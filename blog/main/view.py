#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, make_response, url_for, redirect, abort
from . import main
import os
import sys
#导入上级目录的文件
#out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(out)
#import app, model

#注意要用蓝图的‘main’
@main.route('/')
def v_index():
    return render_template('index.html', title="fuzzier's Rss")

@main.route('/about_me')
def v_about_me():
    return render_template('about_me.html')
