#Reverse a integer number
#Given:
#76542
#
#Expected output:
#24567

num = 76542
reversed_num = 0
while num > 0:
    reversed_num = (reversed_num * 10) + num % 10
    num //= 10

print("reversed number:", reversed_num)
