
"""
this is function  description 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from app.controller.parkingController import ParkingController
from wtforms.validators import DataRequired, ValidationError


class SearchForm(FlaskForm):
    parkingID = StringField('根据车位号查询', validators=[DataRequired()])
    submit = SubmitField('查询')
    OutID = StringField('根据车位号出场', validators=[DataRequired()])
    outmit = SubmitField('出场')

    def validate_OutID(self, field):
        parkingid = field.data
        print(parkingid)
        if len(ParkingController.get(ParkingID=parkingid)['data']) == 0:
            raise ValidationError("车位号不存在")

class IndexForm(FlaskForm):
    card = SelectField('办卡情况', choices=[(0, '未办卡'), (1, '月卡'), (2, '年卡')], coerce=int)
    submit = SubmitField('入场')
