from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


import os
app = Flask(__name__)
 # 初始化扩展，传入程序实例 app

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getenv('DATABASE_FILE', 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控


login_manager = LoginManager(app)  # 实例化扩展类

db = SQLAlchemy(app) 



@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象
login_manager.login_view = 'login'
@app.context_processor
def inject_user(): #模板上下文处理函数
    user = User.query.first()
    return dict(user=user)



from watchlist.models import User
from watchlist import views, errors, commands
