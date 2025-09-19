#Accept a list of 5 float numbers as an input from the user#

numbers = []

for i in range(1, 6):
    user_num = float(input(f"num{i}: "))
    numbers.append(user_num)

print("list:", numbers)


# or just split one sentece insted of looping 5 times ??
