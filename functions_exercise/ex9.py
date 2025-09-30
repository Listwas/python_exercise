#Find the largest item from list

x = [4, 6, 8, 24, 12, 2]

def find_largest(lst):
    if not lst:
        return None

    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(max(x))
print(find_largest(x))

