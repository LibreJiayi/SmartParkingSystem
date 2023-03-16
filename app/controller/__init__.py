
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dzj:Dzj1365878@rm-2zes1gmjlcey26osclo.mysql.rds.aliyuncs.com:3306/parking-system"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

