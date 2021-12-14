import math
import numpy as np
import statistics
import pandas as pd
import matplotlib.pyplot as plt


#1
data = pd.read_excel('Варианты_загрузка_данных.xls', sheet_name='19', index_col=None, header=0)
data = pd.Series(data.value)

#2
print(data[5])
print(data[6:25])

#3
print(pd.Series.min(data))
print(pd.Series.max(data))

#4
plt.plot(range(0,len(data)),pd.Series.sort_values(data))

#5
mean = pd.Series.mean(data)
mean_m = [item for item in data if item > mean]
print(mean_m)

#6
def intervals(data):
    m = math.ceil(math.sqrt(len(data)))
    xmin = pd.Series.min(data); xmax = pd.Series.max(data);
    h = (xmax - xmin) / m
    inter = [(xmin+h*i, xmin+h*(i+1)) for i in (range(0,m+1))]
    return inter

inter = intervals(data)

for i in range(len(inter)):
    inter_count = 0
    for j in range(len(data)):
        if (data[j] >= inter[i][0]) and (data[j]<=inter[i][1]):
            inter_count += 1
    print ('Intervals %s %s count: %s' %(inter[i][0], inter[i][1], inter_count))
