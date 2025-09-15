#Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536,
#the output shall be “6 3 5 7“, with a space separating the digits.


def reverse_number(num, reversed_num=0):
    if num == 0:
        return reversed_num
    
    last_digit = num % 10
    remaining_num = num // 10
    reversed_num = reversed_num * 10 + last_digit

    return reverse_number(remaining_num, reversed_num)

try:
    number = int(input("number: "))
    print("reversed number:", " ".join(str(reverse_number(number))))
except ValueError:
    print("input is not an integer")

# or just simply:
# number = int(input("number: "))
# reversed_digits = " ".join(str(number)[::-1]
# print(reversed_digits)
