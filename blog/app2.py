#!/usr/bin/python
# -*- coding: utf-8 -*-

# 利用工厂对象创建方式

import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown
#from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

# 定义全局变量
basedir = os.path.abspath(os.path.dirname(__file__))
# nav = Nav()

app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 配置密钥
app.config['SECRET_KEY'] = 'im coming home.'

# flask_login所需配置
from my_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.v_login'  # 设置默认的登录函数

# 初始化插件
db = SQLAlchemy(app)
#login_manager.init_app(app)
bootstrap = Bootstrap(app)
Markdown(app)
# manager = Manager(app)

# 注册蓝图
from main import main as main_blueprint
app.register_blueprint(main_blueprint)
from crawler import crawler as crawler_blueprint
app.register_blueprint(crawler_blueprint, url_prefix='/crawler')
from comment import comment as comment_blueprint
app.register_blueprint(comment_blueprint, url_prefix='/comment')
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
