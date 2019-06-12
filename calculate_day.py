import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read CSV file - creates a data frame called earnings
earnings = pd.read_csv("F:\\POLYU\\Dissertation_data\\datacopy\\LINK_hourtime.csv", encoding = 'utf-8',names=['ID','Trip_id', 'Card_id' , 'On_line_name', 'On_time', 'off_line_name', 'off_time' ,'on_id', 'off_id', 'TRANSFORM' , 'USERODSOURCE','ONTIME','OFFTIME'])

def split_day(t):
    l,r = t.strip().split(' ')
    return l

day = []

for i in earnings.On_time:
    day.append(split_day(i))

earnings['Day'] = day
earnings.to_csv("F:\\POLYU\\Dissertation_data\\datacopy\\LINK_hourtime_1.csv", index=False)