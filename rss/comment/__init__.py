#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

#蓝图名称可以和包名相同
comment = Blueprint('comment', __name__)

import view