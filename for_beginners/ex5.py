#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check_list(x):
    print("your list: ", x)
    first = x[0]
    last = x[-1]

    return first == last

print(check_list(numbers_x))
print(check_list(numbers_y))
