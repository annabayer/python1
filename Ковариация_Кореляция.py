import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import statistics as stat
import math


df = pd.read_excel('k1.xlsx', sheet_name='19', header=0)
avgX1 = stat.mean(df.x1)
avgX2 = stat.mean(df.x2)


def cov(df,x1,x2):
	sum = 0
	for i in range(0, len(df)):
		sumcov = ((x1[i]-avgX1)*(x2[i]-avgX2))
		sum = sum + sumcov
		pass
	cov = sum/(len(df)-1)
	qx1 = math.sqrt(stat.variance(x1))
	qx2 = math.sqrt(stat.variance(x2))
	dis = (cov/(qx1*qx2))
	return dis

print(cov(df,df.x1,df.x2))
print(np.corrcoef(df.x1,df.x2))
print(np.cov(df.x1, df.x2))
