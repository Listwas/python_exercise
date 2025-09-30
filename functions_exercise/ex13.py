#Write a recursive function to calculate the factorial of a non-negative integer.

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

print(factorial(5))
print(factorial(10))
    


