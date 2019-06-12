import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import openpyxl
from pandas import DataFrame
from math import radians, cos, sin, asin, sqrt

Card_ID = 0
on_id = 1
off_id = 2
TRANSFORM  = 3
ONTIME = 4
OFFTIME = 5
Day = 6
X_on = 7
Y_on = 8
X_off = 9
Y_off = 10

def geodistance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
    distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    distance=round(distance/1000,3)
    return distance

def calculate_features(Userdata, distance_day_list, time_day_list):
    
    Userdata.append([0,0,0,0,0,0,0,0,0,0,0])
    UserTData_day = []
    for i in Userdata:
        if len(UserTData_day) == 0:
            UserTData_day.append(i)
        elif (UserTData_day[len(UserTData_day)-1])[Day]== i[Day]:
            UserTData_day.append(i)
        else:
            day_trips = len(UserTData_day)
            time_day = []
            distance_day = []
            
            for j in range(day_trips):
                
                distance = geodistance(UserTData_day[j][X_on], UserTData_day[j][Y_on], UserTData_day[j][X_off], UserTData_day[j][Y_off])
                distance_day.append(distance)
                time = float(float(UserTData_day[j][OFFTIME]) - float(UserTData_day[j][ONTIME]))
                time_day.append(time)

            distance_day_list.append(sum(distance_day))
            time_day_list.append(sum(time_day))
            UserTData_day = []
            UserTData_day.append(i)
    del UserTData_day



if __name__ == '__main__':
    f = open(r'E:\POLYU\AREA\LINK_hourtime_Sorting_new.csv', encoding='utf-8')
    csv_reader_lines = csv.reader(f)
    UserTData = []
    dict_avg_distance_day = {}
    dict_avg_time_day = {}

    for one_line in csv_reader_lines:
        if len(UserTData)==0:
            UserTData.append(one_line)
        elif (UserTData[len(UserTData)-1])[on_id]== one_line[on_id]:
            UserTData.append(one_line)
        else:
            distance_day_list = []
            time_day_list = []

            calculate_features(UserTData, distance_day_list, time_day_list)
            
            onid = UserTData[0][on_id]
            avg_distance_day = round(float(sum(distance_day_list) / len(distance_day_list)), 4) 
            dict_avg_distance_day[onid] = avg_distance_day
            avg_time_day = round(float(sum(time_day_list) / len(time_day_list)), 4)
            dict_avg_time_day[onid] = avg_time_day


            UserTData = []
            UserTData.append(one_line)
    
    del csv_reader_lines
    f.close()

    characteristic = pd.read_csv(r"E:\POLYU\AREA\individual_characteristic_new1.csv", encoding = 'utf-8')
    avg_distance = list(dict_avg_distance_day.values())
    avg_time = list(dict_avg_time_day.values())
    
    characteristic['Day_Distance_Average'] = avg_distance
    characteristic['Day_Time_Average'] = avg_time
    characteristic.to_csv(r"E:\POLYU\AREA\individual_characteristic_new2.csv", index=False)