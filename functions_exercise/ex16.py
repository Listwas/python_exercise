#Use a lambda with the map() function to double each element in a list

numbers = [1, 2, 3, 4, 5]

double = list(map(lambda x: x * 2, numbers))
print(double)
