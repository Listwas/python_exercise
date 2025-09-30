# Use a lambda with the sorted() function to sort a list of tuples based on the second element

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

sorted_data = list(sorted(data, key=lambda x: x[1]))
print(sorted_data)
