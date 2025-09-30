#Create Higher-Order Function
#Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
#
#The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply_operation(func, x, y):
    return func(x, y)

print(apply_operation(add, 2, 3))
print(apply_operation(sub, 2, 3))
print(apply_operation(lambda x, y: x * y, 2, 3))
