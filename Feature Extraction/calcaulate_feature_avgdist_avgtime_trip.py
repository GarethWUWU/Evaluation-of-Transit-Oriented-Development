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

def calculate_features(Userdata, distance_trip_list, time_trip_list):
    
    Userdata.append([0,0,0,0,0,0,0,0,0,0,0])
    trips = len(Userdata)

    for i in range(trips):
                
        distance = geodistance(UserTData[i][X_on], UserTData[i][Y_on], UserTData[i][X_off], UserTData[i][Y_off])
        distance_trip_list.append(distance)
        time = float(float(UserTData[i][OFFTIME]) - float(UserTData[i][ONTIME]))
        time_trip_list.append(time)




if __name__ == '__main__':
    f = open(r'E:\POLYU\AREA\LINK_hourtime_Sorting_new.csv', encoding='utf-8')
    csv_reader_lines = csv.reader(f)
    UserTData = []
    dict_avg_distance_trip = {}
    dict_avg_time_trip = {}

    for one_line in csv_reader_lines:
        if len(UserTData)==0:
            UserTData.append(one_line)
        elif (UserTData[len(UserTData)-1])[on_id]== one_line[on_id]:
            UserTData.append(one_line)
        else:
            distance_trip_list = []
            time_trip_list = []

            calculate_features(UserTData, distance_trip_list, time_trip_list)
            
            onid = UserTData[0][on_id]
            avg_distance_trip = round(float(sum(distance_trip_list) / len(distance_trip_list)), 4) 
            dict_avg_distance_trip[onid] = avg_distance_trip
            avg_time_trip = round(float(sum(time_trip_list) / len(time_trip_list)), 4)
            dict_avg_time_trip[onid] = avg_time_trip


            UserTData = []
            UserTData.append(one_line)
    
    del csv_reader_lines
    f.close()

    characteristic = pd.read_csv(r"E:\POLYU\AREA\individual_characteristic_new2.csv", encoding = 'utf-8')
    avg_distance = list(dict_avg_distance_trip.values())
    avg_time = list(dict_avg_time_trip.values())
    
    characteristic['Trip_Distance_Average'] = avg_distance
    characteristic['Trip_Time_Average'] = avg_time
    characteristic.to_csv(r"E:\POLYU\AREA\individual_characteristic_new3.csv", index=False)