import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




#Read CSV file - creates a data frame called earnings
earnings = pd.read_csv(r"E:\POLYU\LINK_hourtime.csv", encoding = 'utf-8')
'''earnings = earnings.drop('USERODSOURCE', axis=1) 
earnings = earnings.drop('Trip_id', axis=1)  #axis=1 indicates to drop a column (axis=0 is for rows)'''
#Show column headings
print(earnings.head())
on_time = []
off_time = []
day = []

def split_time(t):
    l,r = t.strip().split(' ')
    return r
def split_day(t):
    l,r = t.strip().split(' ')
    return l

def t2h(t):
    h,m,s = t.strip().split(":")
    return int(h)  + round(float(m) / 60 , 4) + round(float(s) / 3600 , 4)


'''for i in range(len(earnings.On_time)-1, -1, -1):
    if ' ' not in earnings.On_time[i]:
        earnings = earnings.drop(index = i, axis=0)  #axis=1 indicates to drop a column (axis=0 is for rows)
        

for i in range(len(earnings.off_time)-1, -1, -1):
    if ' ' not in earnings.off_time[i]:
        earnings = earnings.drop(i, axis=0)  #axis=1 indicates to drop a column (axis=0 is for rows)

earnings.to_csv(r"E:\POLYU\LINK_hourtime.csv", index = False)'''

'''for i in earnings.On_time:
    on_time.append(split_time(i))
for i in range(len(on_time)):
    on_time[i] = t2h(on_time[i])
earnings['ONTIME'] = on_time
'''
'''for i in earnings.off_time:
    off_time.append(split_time(i))
for i in range(len(off_time)):
    off_time[i] = t2h(off_time[i])
earnings['OFFTIME'] = off_time 
earnings.to_csv(r"E:\POLYU\LINK_hourtime.csv", index = False)'''

for i in earnings.On_time:
    day.append(split_day(i))

'''for i in range(len(on_time)):
    on_time[i] = t2h(on_time[i])
    off_time[i] = t2h(off_time[i])

earnings['ONTIME'] = on_time
earnings['OFFTIME'] = off_time '''
earnings['Day'] = day
earnings.to_csv(r"E:\POLYU\LINK_hourtime.csv", index = False)