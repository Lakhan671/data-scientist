# Create the age histogram from the agedata.csv file
# ------------------------------------------------------------

# Import the pyplot
import matplotlib.pyplot as plt
%matplotlib qt
# Open and read the file
f = open('C:/KALS/data science/data scientist/data scientist/dataScince/datavisualization/agedata.csv','r')
agefile = f.readlines()

age_list = []

# Append the list with the age data
for records in agefile:
    age_list.append(int(records))

# Create bins list for histogram
bins = [0,10,20,30,40,50,60,70,80,90,100]

# Change the chart labels
#plt.figure("f.90")
plt.subplot(2,2,1)
plt.title("Age histogram")
plt.xlabel("Group")
plt.ylabel("Age")

# Create the plot
plt.hist(age_list, bins, histtype='bar', rwidth=0.9)
#plt.savefig('C:/KALS/data science/data scientist/data scientist/dataScince/datavisualization\\images/01box2.png')

# Show the Plot
#plt.show()
# -------------------------------------------------------------
# Create the box plot of sales data from the file
# -------------------------------------------------------------


# Open the file in read mode and read lines
f = open('C:\KALS\data science\data scientist\data scientist\dataScince\datavisualization/salesdata.csv','r')
salefile = f.readlines()

# Create the sales List
sale_list = []

# Append all the records from the file to the saleslist
for records in salefile:
    sale_list.append(int(records))

# Change the chart labels
#plt.figure("f.91")
plt.subplot(2,2,2)
plt.title("Box Plot of Sales")

# Create the plot
plt.boxplot(sale_list)
plt.tight_layout()
plt.savefig('C:/KALS/data science/data scientist/data scientist/dataScince/datavisualization\\images/subgrid.png')
plt.co
# Show the Plot
plt.show()
