#Write a Python code to display numbers from a list divisible by 7

list_x = [10, 20, 33, 46, 55]
print("list given: ", list_x)

divisible = []
indivisible = []
for item in list_x:
    if item % 5 == 0:
        divisible.append(item)
    else:
        indivisible.append(item)

print("divisible: ", divisible, "\nindivisible: ", indivisible)


        


