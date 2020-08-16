# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

x_cities=["new york","London","Dubai","New Delhi","Tokyo"]
y_tem=[75,65,105,98,90]
plt.figure("Cites Temperature Chart")
plt.title("Temperature Variantion")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.bar(x_cities,y_tem,color=['r','g','c','y','m'])
plt.savefig('C:/KALS/data science/data scientist/data scientist/dataScince/datavisualization\\images/tem_of_cities.png')
plt.show()



