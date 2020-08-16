cityTemp=open('C:/KALS/data science/data scientist/python/file/citytemp.csv','r')
print("---------------------------")
city1=cityTemp.readline()
city2=cityTemp.readlines()
city,temperature,unit=city1.split(",")
print(city,temperature,unit)
cityTemp=open('C:/KALS/data science/data scientist/python/file/citytemp.csv','a')
#cityTemp.write(city1)
t=0
for x in city2:
     city,temperature,unit=x.split(",")
     t=t+int(temperature);
       
print(t)
