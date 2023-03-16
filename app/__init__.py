
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from app.models import db


def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder="./static")
    # app 读取配置文件
    app.config.from_object(config)

    # 初始化数据库
    db.init_app(app)

    # 给app 添加Bootstrap的支持
    Bootstrap(app)

    from views import index_bp, carlist_bp, history_bp
    app.register_blueprint(index_bp, url_prefix='/')
    app.register_blueprint(carlist_bp, url_prefix='/')
    app.register_blueprint(history_bp, url_prefix='/')

    return app
