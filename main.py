import pandas

# with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as s_data:
#     data=s_data.read()
#     print(data)

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"])

Gray_count=data["Primary Fur Color"].value_counts()["Gray"]
Cinnamon_count=data["Primary Fur Color"].value_counts()["Cinnamon"]
Black_count=data["Primary Fur Color"].value_counts()["Black"]
print(Gray_count)
print(Cinnamon_count)
print(Black_count)
