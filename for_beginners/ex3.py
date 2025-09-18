#Write a Python code to accept a string from the user and display characters present at an even index number.

#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

og_string = input("string: ")
print("Printing only even index chars")
for i in range(len(og_string)):
    if i % 2 == 0:
        print(og_string[i])

