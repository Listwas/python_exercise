#Ask the user for a number. Print this number padded with leading zeros to a width of 5.
#For example, if the input is 12, the output should be “00012“

user_num = input("number: ")

print(f"{int(user_num):05}")
print(user_num.zfill(5))
print(format(int(user_num), '05'))
print("%05d" % int(user_num))


