# -------------------------------------------------------------
# Create the box plot of sales data from the file
# -------------------------------------------------------------

# Import pyplot
import matplotlib.pyplot as plt

# Open the file in read mode and read lines
f = open('C:\KALS\data science\data scientist\data scientist\dataScince\datavisualization/salesdata.csv','r')
salefile = f.readlines()

# Create the sales List
sale_list = []

# Append all the records from the file to the saleslist
for records in salefile:
    sale_list.append(int(records))

# Change the chart labels
plt.title("Box Plot of Sales")

# Create the plot
plt.boxplot(sale_list,
            patch_artist=True,
            boxprops=dict(facecolor='g',color='r',linewidth=2),
            whiskerprops=dict(color='r',linewidth=2),
            medianprops=dict(color='w',linewidth=1),
            capprops=dict(color='k',linewidth=2),
            flierprops=dict(markerfacecolor='r',marker='o',markersize=7)
            )

# Show the Plot
plt.savefig('C:/KALS/data science/data scientist/data scientist/dataScince/datavisualization\\images/boxplot.png')
plt.show()


