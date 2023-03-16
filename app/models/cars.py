from . import Base, db


class Cars(Base):
    __tablename__ = 'cars'

    ID = db.Column(db.Integer, primary_key=True)
    CarID = db.Column(db.String(255, 'utf8_general_ci'), info='车辆id，可认为车牌号')
    StartTime = db.Column(db.DateTime, info='入场时间')
    EndTime = db.Column(db.DateTime, info='出场时间')
    TotalTime = db.Column(db.Integer, info='停车总时间，按小时算')
    AnyCard = db.Column(db.Integer, info='车辆办卡情况，0为未办卡，1为月卡，2为年卡')
    Fee = db.Column(db.Float(255), info='该次停车需要缴纳的费用')
    ParkingID = db.Column(db.Integer, info='车位id')
