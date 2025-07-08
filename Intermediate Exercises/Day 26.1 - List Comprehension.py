#	Challenge 1: Squaring numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]
print(squared_numbers)


#	Challenge 2: Filtering even numbers

result = [num for num in numbers if num & 1 == 0]
print(result)
