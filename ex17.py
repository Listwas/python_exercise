#Generate Fibonacci series up to 15 terms#

num1, num2 = 0, 1

for i in range(15):
    res = num1 + num2
    print(res, end=" ")
    num1 = num2
    num2 = res
