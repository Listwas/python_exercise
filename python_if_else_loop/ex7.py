#Write a Python program to print the reverse number pattern using a for loop.

#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1

for i in range(5):
    for j in range(5-i, 0, -1):
        print(j, end=" ")
    print()
