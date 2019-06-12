with open(r'E:\POLYU\LINK_OD_201605_WEEKDAY_7_MIN_E.csv','ab') as f:
    f.write(open(r'E:\POLYU\LINK_OD_201605_WEEKDAY_7_MAX_E.csv','rb').read())#将2.csv内容追加到1.csv的后面