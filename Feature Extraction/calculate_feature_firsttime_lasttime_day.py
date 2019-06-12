import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import openpyxl
from pandas import DataFrame

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


def calculate_features(Userdata, first_time_weekday_list, last_time_weekday_list,trips_weekday_list):
    
    Userdata.append([0,0,0,0,0,0,0,0,0,0,0])
    UserTData_day = []
    for i in Userdata:
        if len(UserTData_day) == 0:
            UserTData_day.append(i)
        elif (UserTData_day[len(UserTData_day)-1])[Day]== i[Day]:
            UserTData_day.append(i)
        else:
            day_trips = len(UserTData_day)
            trips_weekday_list.append(day_trips)
            on_time_day = []
            off_time_day = []
            
            for j in range(day_trips):
                
                on_time = float(UserTData_day[j][ONTIME])
                if on_time <= 4:
                        on_time += 24
                on_time_day.append(on_time)
                off_time = float(UserTData_day[j][OFFTIME])
                if off_time <= 4 :
                        off_time += 24
                off_time_day.append(off_time)

            first_time_weekday_list.append(min(on_time_day))
            last_time_weekday_list.append(max(off_time_day))
            UserTData_day = []
            UserTData_day.append(i)
    del UserTData_day



if __name__ == '__main__':
    f = open(r'E:\POLYU\AREA\LINK_hourtime_Sorting_new.csv', encoding='utf-8')
    csv_reader_lines = csv.reader(f)
    UserTData = []
    dict_first_time_weekday = {}
    dict_last_time_weekday = {}
    dict_trips_weekday = {}

    for one_line in csv_reader_lines:
        if len(UserTData)==0:
            UserTData.append(one_line)
        elif (UserTData[len(UserTData)-1])[on_id]== one_line[on_id]:
            UserTData.append(one_line)
        else:
            first_time_weekday_list = []
            last_time_weekday_list = []
            trips_weekday_list = []
            calculate_features(UserTData, first_time_weekday_list, last_time_weekday_list,trips_weekday_list)
            
            onid = UserTData[0][on_id]
            first_average_weekday = round(float(sum(first_time_weekday_list) / len(first_time_weekday_list)), 4) 
            dict_first_time_weekday[onid] = first_average_weekday
            last_average_weekday = round(float(sum(last_time_weekday_list) / len(last_time_weekday_list)), 4)
            dict_last_time_weekday[onid] = last_average_weekday
            trips_average_weekday = round(float(sum(trips_weekday_list) / len(trips_weekday_list)), 4)
            dict_trips_weekday[onid] = trips_average_weekday

            UserTData = []
            UserTData.append(one_line)
    
    del csv_reader_lines
    f.close()

    characteristic = pd.read_csv(r"E:\POLYU\AREA\individual_characteristic.csv", encoding = 'utf-8')
    first_time = list(dict_first_time_weekday.values())
    last_time = list(dict_last_time_weekday.values())
    trips = list(dict_trips_weekday.values())
    characteristic['First_Trip_Time_Average'] = first_time
    characteristic['Last_Trip_Time_Average'] = last_time
    characteristic['Trips_Average'] = trips
    characteristic.to_csv(r"E:\POLYU\AREA\individual_characteristic_new1.csv", index=False)





        
