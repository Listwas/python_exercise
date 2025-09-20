#Write a Python program to count the total number of digits in a number using a while loop.

#For example, the number is 75869, so the output should be 5

usr_num = int(input("your number: "))

count = 0
while usr_num != 0:
    usr_num //= 10
    count += 1

print(f"your number has {count} digits")
