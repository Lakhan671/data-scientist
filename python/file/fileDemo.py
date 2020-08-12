cityTemp=open('C:/KALS/data science/data scientist/python/file/citytemp.csv','r')
print("---------------------------")
city1=cityTemp.readline()
city2=cityTemp.readlines()
city,temperature,unit=city1.split(",")
print(city,temperature,unit)

