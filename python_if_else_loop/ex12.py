#Display Fibonacci series up to 10 terms

current_num = 0
previous_num = 1
for i in range(10):
    print(current_num)
    res = current_num + previous_num
    current_num = previous_num
    previous_num = res
