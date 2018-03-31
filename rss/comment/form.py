#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentForm(Form):
    theme = SelectField('Theme', choices=[('0', u'douban'), ('1', u'damai'), ('2', u'dy2018')])
    body = TextAreaField("TextArea", default="please add content")
    submit = SubmitField('Put')
