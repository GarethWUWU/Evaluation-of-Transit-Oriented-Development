import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import openpyxl
from pandas import DataFrame
#Read CSV file - creates a data frame called earnings
data = pd.read_csv(r"E:\POLYU\LINK_hourtime_Sorting_new1.csv", encoding = 'utf-8',  names=['Card_ID', 'on_id', 'off_id', 'TRANSFORM' , 'ONTIME','OFFTIME','Day','ON_X', 'ON_Y', 'OFF_X', 'OFF_Y'])
data_change = data.sort_values(by = ['on_id','Day'], axis = 0, ascending = True)
data_change.to_csv(r"E:\POLYU\AREA\LINK_hourtime_Sorting_new.csv", index=False)