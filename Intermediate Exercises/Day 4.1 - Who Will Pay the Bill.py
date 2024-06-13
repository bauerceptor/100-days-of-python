namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

import random

random_pick = random.randint(0, len(names)-1)

print(random_pick)

print(f"{names[random_pick]} is going to buy the meal today!")