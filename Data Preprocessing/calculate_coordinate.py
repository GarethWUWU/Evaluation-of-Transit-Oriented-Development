import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import openpyxl
from pandas import DataFrame
import geopandas as gpd

earnings = pd.read_csv(r"E:\POLYU\LINK_hourtime_Sorting_n.csv", encoding = 'utf-8')
earnings = earnings[['Card_ID','on_id','off_id','TRANSFORM','ONTIME','OFFTIME','Day','X_on','Y_on']]
coordinate = gpd.read_file(r"C:\Users\king\Desktop\Desertation\sample_data\Jiawei\Beijing Grid\bj_grid500m_wgs84.shp")
print(coordinate.head())
coordinate = coordinate[["AREA_ID", "X",'Y']]

earnings = pd.merge(earnings, coordinate, left_on="off_id", right_on="AREA_ID",sort = False)
earnings.to_csv(r"E:\POLYU\LINK_hourtime_Sorting_new.csv", index=False)
#earnings.rename(columns={"X": "X_on", "Y": "Y_on"}, inplace = True)

#earnings = pd.merge(earnings, coordinate, left_on="off_id", right_on="AREA_ID")
#print(earnings.head())
#earnings.to_csv(r"E:\POLYU\LINK_hourtime_Sorting_new.csv", index=False)