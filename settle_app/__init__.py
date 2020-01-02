from flask import Flask

from settle_app.Controller.StatementAccountController import account
from settle_app.config.Config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

print("默认启动配置项")
settle_app = Flask(__name__)

# 配置多模块route路由
settle_app.register_blueprint(account, url_prefix='/api/settle/account')

# 配置数据库信息
settle_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# settle_app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
settle_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# settle_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db = SQLAlchemy(settle_app)
# 创建数据库及连接
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# # 创建DBSession类型:
# dBSession = sessionmaker(bind=engine)
# # dBSession = DBSession()

