# with open("weather_data.csv","r") as weather:
#     weather_week=weather.readlines()
#     print(weather_week)
#
# import csv
#
# with open("weather_data.csv","r") as weather:
#     weather_week=csv.reader(weather)
#     temperatures=[]
#     i=0
#     for row in weather_week:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data)