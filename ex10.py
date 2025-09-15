#Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("given lists")
print(f"list1: {list1}\nlist2: {list2}")

odd_even = [item for item in list1 if item % 2 != 0] + [item for item in list2 if item %2 == 0]

print("result:", odd_even)
    
