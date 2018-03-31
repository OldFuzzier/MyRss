#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, redirect
from . import crawler
from damai import main_damai
from douban import main_douban
from dy2018 import main_dy2018


@crawler.route('/douban_recent')
def v_douban():
    try:
        info_lst = main_douban()
        return render_template('douban.html', info_lst=info_lst)
    except:
        return render_template('404.html'), 404


@crawler.route('/damai_recent')
def v_damai():
    try:
        info_lst = main_damai()
        return render_template('damai.html', info_lst=info_lst)
    except:
        return render_template('404.html'), 404


@crawler.route('/dy2018_recent')
def v_dy2018():
    try:
        info_lst = main_dy2018()
        return render_template('dy2018.html', info_lst=info_lst)
    except:
        return render_template('404.html'), 404


