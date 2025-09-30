#Create an inner function
#Define an outer function that accepts two parameters, a and b.
#Inside this outer function, define an inner function that calculates the sum of a and b.
#The outer function should then add 5 to this sum.
#Finally, the outer function should return the resulting value.”

def outer(a, b):
    def inner(a, b):
        return a + b
    sum = inner(a, b)
    return sum + 5

print(outer(5, 5))
