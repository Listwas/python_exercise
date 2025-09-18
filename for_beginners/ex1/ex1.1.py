#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.



def multiplication_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2

num1 = int(input("num1: "))
num2 = int(input("num2: "))
result = multiplication_or_sum(num1, num2)

print("result is: ", result)
