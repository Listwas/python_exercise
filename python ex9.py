#Write a Python code to check if the given number is a palindrome. 
#A palindrome number reads the same forwards and backward. 
#For example, 545 is a palindrome number.

def is_palindrome(num):
    new_num = str(num)
    if len(new_num) == 0:
        return palindrome

    print(new_num, new_num[1:], new_num[:-1], new_num[1:-1])
    first = new_num[:1]
    last = new_num[:-1]
    print(first, last)


num = int(input("number: "))

print(is_palindrome(num))
