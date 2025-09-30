#Create a recursive function
#Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

def recur(num):
    if not num:
        return 0
    return num + recur(num - 1)
    
print(recur(10))
