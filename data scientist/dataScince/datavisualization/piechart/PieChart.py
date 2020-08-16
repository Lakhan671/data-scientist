# ------------------------------------------------------------
# Create the pie chart from the given sales data in a file
# ------------------------------------------------------------

# import pyplot
import matplotlib.pyplot as plt

# Open the file and read the data
f = open('C:\KALS\data science\data scientist\data scientist\dataScince\datavisualization\piechart//agedata.csv','r')
agefile = f.readlines()

# Load the records to a list and split them to create list of cities
city_list = []

for records in agefile:
    age, city = records.split(sep=',')
    city_list.append(city)
    
# Create a dictionary of City Names and Total count per city
from collections import Counter
city_count = Counter(city_list)

# Unpack city names and total count to respective lists
city_names = list(city_count.keys())
city_values = list(city_count.values())

#Create the pie chart
plt.title("Age pie chart( created by Lakhan Singh)")
plt.pie(city_values, labels=city_names, autopct='%.2f%%')
plt.show()


