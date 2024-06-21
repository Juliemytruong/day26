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
import statistics

data=pandas.read_csv("weather_data.csv")
data_dic=data.to_dict()
print(data_dic)
temp_list=data["temp"].to_list()
print(temp_list)
average_temp=statistics.mean(temp_list)
print(average_temp)
