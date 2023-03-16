#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:carlistviews.py
# author:ZCJ
# datetime:2022/6/24 19:33
# software: PyCharm

"""
this is function  description 
"""

from flask import render_template, redirect, request, session, flash
from forms import SearchForm
from app.controller.carsController import CarsController
from app.controller.parkingController import ParkingController
from . import carlist_bp


@carlist_bp.route('/carlist', methods=['GET', 'POST'])
def carlist():
    import app.service.services
    TheCar = ParkingController.get()['data']
    form = SearchForm()
    if request.method=='POST':
        if form.parkingID.data:
            parkingID = form.parkingID.data
            form.parkingID.data = ''
            TheCar = ParkingController.get(ParkingID=parkingID)['data']
        elif form.OutID.data:
            OutID = int(form.OutID.data)
            form.OutID.data = ''
            if len(ParkingController.get(ParkingID=OutID)['data']) != 0:
                car_id = ParkingController.get(ParkingID=OutID)['data'][0]['CarID']
                app.service.services.get_out(OutID)
                session['con'] = '离开'
                return render_template('carlist.html', carid=car_id, innout=session['con'], form=form, carlist=TheCar)
            else:
                flash('该车位不存在')
                return redirect('carlist')
    return render_template('carlist.html', form=form, carlist=TheCar, carid='没有', innout='进出')
