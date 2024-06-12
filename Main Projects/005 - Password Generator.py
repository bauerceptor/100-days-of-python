#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
    
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# print(password)       # uncomment it for easy

# method 1 for shuffling - hard mode

list = []

list.extend(password)
random.shuffle(list)
result_shuffle = ''.join(list)

print(result_shuffle)

# method 2 for shuffling - hard mode

random_password = ''.join(random.sample(password, len(password)))

print(random_password)