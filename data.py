# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:45:58 2017

@author: Eyshika Agarwal
"""
import numpy as np
from pandas import *
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
#import datetime
import plotly.plotly as py
data=read_csv('Rpi_data - Sheet1 .csv')
time=data['Time']
x=data['CPU Usage']
y=data['Temperature']
z=data['Temperature']

plt.plot_date(time,x, 'b-',label="CPU Usage")
plt.plot_date(time,y, 'g-', label="Temperature")
plt.gcf().autofmt_xdate()
plt.title('Time Series')
plt.xlabel('Date/Time')
plt.legend(fontsize= 'x-small')
plt.show()
bins=[0,10,20,30,40,50,60,70,80,90]
plt.hist(x,bins, normed=True, histtype='bar', rwidth=0.9)
plt.title("Histogram of CPU Usage")
plt.xlabel('CPU Usage')
plt.gcf()
plt.show()

plt.hist(y,bins, normed=1, histtype='bar', rwidth=0.9)
plt.title("Histogram of Temperature")
plt.xlabel('Temperature')
plt.gcf()
plt.show()
data.boxplot(grid=True)
plt.title('Box Plot')
fig, ax=plt.subplots()
fit=np.polyfit(x,y, deg=1)
ax.plot(x, fit[0]*x+fit[1],color='red', label='line regression''Temperature')
ax.scatter(x,y)
plt.title('Scatter Plot with Line Regression')
plt.xlabel('CPU Usage')
plt.legend( fontsize='x-small')
plt.ylabel('Temperature')
fig.show()

lr = linear_model.LinearRegression()
#x.reshape(909,1)
#y.reshape(909,1)
# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, np.transpose(np.matrix(x)),np.transpose(np.matrix(y)), cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.title('Cross Validation')
plt.show()