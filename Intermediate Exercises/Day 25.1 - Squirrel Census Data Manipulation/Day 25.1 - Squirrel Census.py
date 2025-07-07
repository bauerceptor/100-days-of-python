import pandas

data = pandas.read_csv('./Squirrel_Census_Data.csv')
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [],
}

for color in data_dict["Fur Color"]:
    series = data[data['Primary Fur Color'] == color]
    data_dict["Count"].append(len(series))

pandas.DataFrame(data=data_dict).to_csv('squirrel_count.csv')