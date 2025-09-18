#Check if a user-entered string contains any digits using a for loop

def check_string(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

user_input = input("your string: ")
print(f"your string has: {check_string(user_input)} digits")
