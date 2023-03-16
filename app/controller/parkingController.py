#!/usr/bin/env python
# -*- coding:utf-8 -*-


import datetime
import math

from ..models import db
from ..models.parking import Parking



class ParkingController(Parking):

    # add
    @classmethod
    def add(cls, **kwargs):        
        try:
            model = Parking(
                ParkingID=kwargs.get('ParkingID'),
                CarID=kwargs.get('CarID'),
                StartTime=kwargs.get('StartTime'),
                AnyCard=kwargs.get('AnyCard'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ParkingID': model.ParkingID,
                
            }
            return {'app': "200", 'message': "成功！", 'data': results}

        except Exception as e:
            db.session.rollback()
            
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # get
    @classmethod
    def get(cls, **kwargs):        
        try:
            filter_list = []
            if kwargs.get('ParkingID') is not None:
                filter_list.append(cls.ParkingID == kwargs.get('ParkingID'))
            if kwargs.get('CarID'):
                filter_list.append(cls.CarID == kwargs.get('CarID'))
            if kwargs.get('StartTime'):
                filter_list.append(cls.StartTime == kwargs.get('StartTime'))
            if kwargs.get('AnyCard') is not None:
                filter_list.append(cls.AnyCard == kwargs.get('AnyCard'))
            
            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 200))

            parking_info = db.session.query(cls).filter(*filter_list)

            count = parking_info.count()
            pages = math.ceil(count / size)
            parking_info = parking_info.limit(size).offset((page - 1) * size).all()

            results = cls.to_dict(parking_info)
            return {'app': "200", 'message': "成功！", 'totalCount': count, 'totalPage': pages, 'data': results}

        except Exception as e:
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # delete
    @classmethod
    def delete(cls, **kwargs):        
        try:
            filter_list = []
            filter_list.append(cls.ParkingID == kwargs.get('ParkingID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            if not res.first():
                return {'app': "5001", 'message': "数据库错误", 'error': "数据不存在"}
                
            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ParkingID': res.first().ParkingID,
                
            }
            res.delete()
            db.session.commit()

            return {'app': "200", 'message': "成功！", 'data': results}

        except Exception as e:
            db.session.rollback()
            
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # update
    @classmethod
    def update(cls, **kwargs):        
        try:
            filter_list = []
            filter_list.append(cls.ParkingID == kwargs.get('ParkingID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            if not res.first():
                return {'app': "5001", 'message': "数据库错误", 'error': "数据不存在"}
                
            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ParkingID': res.first().ParkingID,
                
            }

            res.update(kwargs)
            db.session.commit()

            return {'app': "200", 'message': "成功！", 'data': results}

        except Exception as e:
            db.session.rollback()
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()
