#Print multiplication table from 1 to 10


for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row*col:4}", end="")
    print()
