#Write all content of a file into a new file by skipping line number 5

with open("test.txt", "r") as f: 
    lines = f.readlines()

with open("new_file.txt", "w") as f:
    for line in lines:
        if line != "line5\n":
            f.write(line)
