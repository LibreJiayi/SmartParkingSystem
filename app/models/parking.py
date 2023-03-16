# coding: utf-8
from . import db, Base


class Parking(Base):
    __tablename__ = 'parking'

    ParkingID = db.Column(db.Integer, primary_key=True, info='车位id(0~100)')
    CarID = db.Column(db.String(255, 'utf8_general_ci'), info='车辆ID')
    StartTime = db.Column(db.DateTime, info='入场时间')
    AnyCard = db.Column(db.Integer, info='车辆办卡情况，0为未办卡，1为月卡，2为年卡')
