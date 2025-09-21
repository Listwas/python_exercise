#Find the sum of a series of a number up to n terms
#Write a program to calculate the sum of this series up to n terms. For example, if the number is 2 and the number of terms is 5, then the series will be 2+22+222+2222+22222=2469

num = 2
terms = 5

num_sum = 0
for i in range(terms):
    print(num, end="")
    num_sum += num

    if i < terms - 1:
        print(" + ", end="")
    
    num = num * 10 + 2

print(" =", num_sum)

