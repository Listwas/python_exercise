#Write a Python program to use for loop to find the factorial of a given number.
#
#The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.
usr_num = int(input("your num: "))
num = 1
for i in range(usr_num, 1, -1):
    num *= i

print("factorial:", num)
