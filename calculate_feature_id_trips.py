import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import openpyxl
from pandas import DataFrame

dict_name = {}

f = open(r'E:\POLYU\AREA\LINK_hourtime_Sorting_new.csv', encoding='utf-8')
csv_reader_lines = csv.reader(f)

for one_line in csv_reader_lines:
    dict_name[one_line[1]] = dict_name.get(one_line[1], 0) + 1


f.close()
ON_ID = list(dict_name.keys())
Number_Trips = list(dict_name.values())
characteristic = pd.DataFrame({'ON_ID':ON_ID,'Number_Trips':Number_Trips})
characteristic.to_csv(r"E:\POLYU\AREA\individual_characteristic.csv", index=False)
