#Write a Python code to check if the given number is a palindrome. 
#A palindrome number reads the same forwards and backward. 
#For example, 545 is a palindrome number.

def is_palindrome(num):
    str_num = str(num)
    reversed_num = str_num[::-1]

    return str_num == reversed_num:

num = int(input("number: "))
print(is_palindrome(num))
