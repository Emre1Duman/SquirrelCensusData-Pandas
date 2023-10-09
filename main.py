#Using squirrel data from an external csv, to create a new csv with data containing only the squirral colours and thier count
import pandas

#Method 1: With lists and loop
squirrel_data = pandas.read_csv("/Users/emre/Documents/Code/100DaysOfPython/Day21-30/Day25/Squirrel Census Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors_list = squirrel_data["Primary Fur Color"].to_list()

grey = 0
red = 0
black = 0

for color in squirrel_colors_list:
    if color == "Gray":
        grey += 1
    if color == "Cinnamon":
        red += 1
    if color == "Black":
        black += 1

squirrel_colors_dic = {
    "fur color": ["gray", "red", "black"],
    "count": [grey, red, black]
}

squirrel_colors = pandas.DataFrame(squirrel_colors_dic)
squirrel_colors.to_csv("squirrel_count.csv")

#Method 2: Less code

data = pandas.read_csv("/Users/emre/Documents/Code/100DaysOfPython/Day21-30/Day25/Squirrel Census Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count2.csv")



