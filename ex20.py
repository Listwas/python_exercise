#Print Reverse Number Pattern

def print_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print()

user_input = int(input("range: "))
print_pattern(user_input)
