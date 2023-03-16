#!/usr/bin/env python
# -*- coding:utf-8 -*-


import datetime
import math

from ..models import db
from ..models.cars import Cars


class CarsController(Cars):

    # add
    @classmethod
    def add(cls, **kwargs):        
        try:
            model = Cars(
                ID=kwargs.get('ID'),
                CarID=kwargs.get('CarID'),
                StartTime=kwargs.get('StartTime'),
                EndTime=kwargs.get('EndTime'),
                TotalTime=kwargs.get('TotalTime'),
                AnyCard=kwargs.get('AnyCard'),
                Fee=kwargs.get('Fee'),
                ParkingID=kwargs.get('ParkingID'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ID': model.ID,
                
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
            if kwargs.get('ID') is not None:
                filter_list.append(cls.ID == kwargs.get('ID'))
            if kwargs.get('CarID'):
                filter_list.append(cls.CarID == kwargs.get('CarID'))
            if kwargs.get('StartTime'):
                filter_list.append(cls.StartTime == kwargs.get('StartTime'))
            if kwargs.get('EndTime'):
                filter_list.append(cls.EndTime == kwargs.get('EndTime'))
            if kwargs.get('TotalTime') is not None:
                filter_list.append(cls.TotalTime == kwargs.get('TotalTime'))
            if kwargs.get('AnyCard') is not None:
                filter_list.append(cls.AnyCard == kwargs.get('AnyCard'))
            if kwargs.get('Fee') is not None:
                filter_list.append(cls.Fee == kwargs.get('Fee'))
            if kwargs.get('ParkingID') is not None:
                filter_list.append(cls.ParkingID == kwargs.get('ParkingID'))
            
            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 200))

            cars_info = db.session.query(cls).filter(*filter_list)

            count = cars_info.count()
            pages = math.ceil(count / size)
            cars_info = cars_info.limit(size).offset((page - 1) * size).all()

            results = cls.to_dict(cars_info)
            print(results)
            return {'app': "200", 'message': "成功！", 'totalCount': count, 'data': results}

        except Exception as e:
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # delete
    @classmethod
    def delete(cls, **kwargs):        
        try:
            filter_list = []
            filter_list.append(cls.CarID == kwargs.get('CarID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            if not res.first():
                return {'app': "5001", 'message': "数据库错误", 'error': "数据不存在"}
                
            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ID': res.first().ID,
                
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
            filter_list.append(cls.ID == kwargs.get('ID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            if not res.first():
                return {'app': "5001", 'message': "数据库错误", 'error': "数据不存在"}
                
            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ID': res.first().ID,
                
            }

            res.update(kwargs)
            db.session.commit()

            return {'app': "200", 'message': "成功！", 'data': results}

        except Exception as e:
            db.session.rollback()
            return {'app': "5001", 'message': "数据库错误", 'data': {'error': str(e)}}
        finally:
            db.session.close()
