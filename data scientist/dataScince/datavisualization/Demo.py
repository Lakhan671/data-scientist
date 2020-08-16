# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

%matplotlib qt
x_days=[1,2,3,4,5]
y_price1=[9,9.5,10.1,10,12]
y_price2=[11,12,10.5,11.5,12.5]
#plot the line plot
plt.title("Stock movement")
plt.xlabel("week days")
plt.ylabel("price in usd")
plt.plot(x_days,y_price1,label="stock 1")
plt.plot(x_days,y_price2,label="stock 2")
plt.legend(loc=4,fontsize=12)
plt.show()
