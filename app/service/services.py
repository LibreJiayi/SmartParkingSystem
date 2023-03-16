import datetime
import time
import random
import re
from start import app
from app.controller.carsController import CarsController
from app.controller.parkingController import ParkingController


# 随机生成车牌号
def car_num():
    """
    随机生成车牌号，先随机生成一个省份简称，然后随机生成一个大写字母，
    最后五位序列号为数字与字母的结合，但字母最多只能出现一次。
    :return: 一个随机的车牌号
    """
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，为了区别0和1
    char2 = '1234567890ABCDEFGHJKLMNPQRSTUVWXYZ'
    char3 = '1234567890'
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    len3 = len(char3) - 1
    while True:
        code = ''
        index0 = random.randint(1, len0)
        index1 = random.randint(1, len1)
        code += char0[index0]
        code += char1[index1]
        code += ' '
        for i in range(1, 5):
            index2 = random.randint(1, len2)
            code += char2[index2]
        index3 = random.randint(1, len3)
        code += char3[index3]
        test = re.match('^.\w.[A-Z]\d{4}$|^.\w.\d[A-Z]\d{3}$|^.\w.\d{2}[A-Z]\d{2}$|^.\w.\d{3}[A-Z]\d$|^.\w.\d{5}$',
                        code)  # 正则表达式，筛选出后五位序列号最多只有一位的车牌号
        if test:
            return code


# 随机生成时间
def get_time():
    """
    在一定的时间跨度中随机生成一个时间
    :return: 一个随机时间
    """
    # 设置开始时间和和结束时间
    min_time = datetime.datetime(2022, 6, 13, 6, 0, 0)
    max_time = datetime.datetime(2022, 6, 13, 23, 0, 0)
    # 时间转换为时间元组，再转换为时间戳
    min_time_t = int(time.mktime(min_time.timetuple()))
    max_time_t = int(time.mktime(max_time.timetuple()))
    # 在时间段中随机一个时间戳，并将其转化为日期时间
    random_t = random.randint(min_time_t, max_time_t)
    random_time = datetime.datetime.fromtimestamp(random_t)
    return random_time


# 计算本次停车费用
def get_fee(result):
    """
    根据车辆信息获取汽车的入场时间，根据入场时间获得一个大于入场时间的时间作为出场时间，
    在计算停车时间和停车费用。
    :param result: 车辆信息
    :return: 包含车位号、出场时间、停车时间、停车费的字典
    """
    start = result[0]['StartTime']
    parking_id = result[0]['ParkingID']
    info = result[0]['AnyCard']
    while True:
        end = get_time()
        if end > start:
            break
    total_time = int((end - start).days * 24 + (end - start).seconds / 3600)
    if info == 0:
        fee = total_time * 100
    elif info == 1:
        fee = total_time * 100 * 0.9
    else:
        fee = total_time * 100 * 0.8
    kwargs = {
        'ParkingID': parking_id,
        'EndTime': end,
        'TotalTime': total_time,
        'Fee': fee
    }
    return kwargs


# 车辆入场
def get_in(info=0, num=''):
    """
    随机生成车辆信息
    :param info:输入车辆办卡情况info(0为未办卡，1为月卡，2为年卡), 车牌号.
    :return:车辆信息
    """
    if num == '':
        num = car_num()
    times = get_time()
    while True:
        parking_id = random.randint(1, 200)
        res = ParkingController.get(**{'ParkingID': parking_id})
        if res.get('app') == '5001' or res.get("totalCount") > 0:
            continue
        else:
            kwargs = {
                    'ParkingID': parking_id,
                    'CarID': num,
                    'StartTime': times,
                    'AnyCard': info
                }
            ParkingController.add(**kwargs)
            break
    return kwargs
    # with app.app_context():
    #     if num == '':
    #         num = car_num()
    #     times = get_time()
    #     while True:
    #         parking_id = random.randint(1, 200)
    #         res = ParkingController.get(**{'ParkingID': parking_id})
    #         if res.get('app') == '5001' or res.get("totalCount") > 0:
    #             continue
    #         else:
    #             kwargs = {
    #                 'ParkingID': parking_id,
    #                 'CarID': num,
    #                 'StartTime': times,
    #                 'AnyCard': info
    #             }
    #             ParkingController.add(**kwargs)
    #             break
    #     return kwargs


# 车辆出场
def get_out(parking_id=0):
    """
    输入车位号，将车位号上的汽车出场并计算停车费
    :param parking_id:车位号
    :return:车位号是否空闲
    """
    with app.app_context():
        res = ParkingController.get(**{'ParkingID': parking_id})
        if res.get('totalCount') > 0:
            result = res.get('data')
            fee = get_fee(result)
            kwargs = {
                'ParkingID': parking_id,
                'CarID': result[0]['CarID'],
                'StartTime': result[0]['StartTime'],
                'AnyCard': result[0]['AnyCard'],
                'EndTime': fee.get('EndTime'),
                'TotalTime': fee.get('TotalTime'),
                'Fee': fee.get('Fee')
            }
            ParkingController.delete(**{'ParkingID': parking_id})
            CarsController.delete(CarID=result[0]['CarID'])
            CarsController.add(**kwargs)
            return True
        else:
            return False


# 获取车位状态
def get_parking():
    """
    获取车位状态和空闲车位数量
    :return: 车位状态和空闲车位数量
    """
    with app.app_context():
        res = ParkingController.get(**{})
        parking_list = []
        count = res.get('totalCount')
        for data in res.get('data'):
            parking_list.append(data['ParkingID'])
        kwargs = {
            'used': count,
            'parking': parking_list,
            'free': 100 - count
        }
        return kwargs


# 获取全部费用
def all_fee():
    """
    获取长期车的总费用，并返回结果。
    :return: 一个字典列表[{'CarID:','Fee:','AnyCard'}]
    """
    with app.app_context():
        fee_month = {}
        fee_year = {}
        res1 = CarsController.get(**{'AnyCard': 1})
        result = res1.get('data')
        for data in result:
            num = data['CarID']
            if num in fee_month:
                fee_month[num] += data['Fee']
            else:
                fee_month[num] = data['Fee']
        res2 = CarsController.get(**{'AnyCard': 2})
        result = res2.get('data')
        for data in result:
            num = data['CarID']
            if num in fee_year:
                fee_year[num] += data['Fee']
            else:
                fee_year[num] = data['Fee']
        fee_list = []
        for num, fee in fee_month.items():
            fee_list.append({'CarID': num, 'Fee': fee, 'AnyCard': 1})
        for num, fee in fee_year.items():
            fee_list.append({'CarID': num, 'Fee': fee, 'AnyCard': 2})
        return fee_list


# 获取停车场车辆停车历史记录
def get_history(car_id=None):
    """
    根据车牌号查找历史记录，默认查找所有记录
    :param car_id: 车牌号（默认为所有车辆）
    :return: 存储历史记录的字典列表
    """
    with app.app_context():
        res = CarsController.get(**{'CarID': car_id})
        return res.get('data')

