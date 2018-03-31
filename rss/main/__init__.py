#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint

#蓝图名称可以和包名相同
main = Blueprint('main', __name__)

import view