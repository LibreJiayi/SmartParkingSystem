#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:indexviews.py
# software: PyCharm

"""
this is function  description 
"""
import random

from flask import render_template, session
from app.controller.parkingController import ParkingController
from app.controller.carsController import CarsController
from forms import IndexForm
from . import index_bp


@index_bp.route('/', methods=['GET', 'POST'])
def index():
    import app.service.services

    car_id = app.service.services.car_num()
    start_time = app.service.services.get_time()
    parking_id = random.randint(1, 200)
    in_car = {
        'CarID': car_id,
        'StartTime': start_time,
        'ParkingID': parking_id,
        'AnyCard': None
    }
    form = IndexForm()
    parked = ParkingController.get()['totalCount']
    rest = 200 - parked
    if form.validate_on_submit():
        parked = ParkingController.get()['totalCount']
        rest = 200 - parked
        card = form.card.data
        in_car['AnyCard'] = card
        CarsController.add(**in_car)
        ParkingController.add(**in_car)
        session['con'] = '进入'
        return render_template('index.html', carid=in_car['CarID'], innout=session['con'], form=form, parked=parked,
                               rest=rest)
    return render_template('index.html', form=form, parked=parked, rest=rest, carid='没有', innout='进出')
