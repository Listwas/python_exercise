#Read Line Number 4 from File

with open("test.txt", "r") as f:
    lines = f.readlines()

    print(lines[2])

