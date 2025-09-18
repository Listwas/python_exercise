#Check Palindrome Number (using while loop)

def is_palindrome(number):
    og_num = number
    reversed_num = 0

    while number > 0:
        last_digit = number % 10
        reversed_num = (reversed_num * 10) + last_digit
        number //= 10

    return og_num == reversed_num



user_input = int(input("number to check: "))

print(is_palindrome(user_input))
