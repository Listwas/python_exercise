#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#

def main():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    sum = num1 * num2

    if sum <= 1000:
        return f"{num1} * {num2} = {sum}"
    else:
        return f"{num1} + {num2} = {num1 + num2}"

print(main())
