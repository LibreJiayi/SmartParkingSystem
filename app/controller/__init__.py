
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 使用 SQLite 作为本地数据库
SQLALCHEMY_DATABASE_URI = "sqlite:///your_local_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()



