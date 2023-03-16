#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:historyviews.py
# author:ZCJ
# datetime:2022/6/30 14:10
# software: PyCharm

"""
this is function  description 
"""

from flask import render_template, redirect, url_for, request
from forms import SearchForm
from app.controller.carsController import CarsController
from app.controller.parkingController import ParkingController
from . import history_bp


@history_bp.route('/history', methods=['GET', 'POST'])
def history():
    import app.service.services
    TheCar = CarsController.get()['data']
    form = SearchForm()
    if request.method == 'POST':
        if form.parkingID.data:
            parkingID = form.parkingID.data
            form.parkingID.data = ''
            TheCar = CarsController.get(ParkingID=parkingID)['data']
    return render_template('history.html', form=form, carlist=TheCar)
