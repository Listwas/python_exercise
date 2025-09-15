#Write a Python code to find how often the substring “Emma” appears in the given string.

search_for = input("string to search for: ")
sentece = input("sentence to serach in: ")

s = sentece.split()

count = 0
for i in s:
    if i == search_for:
        count += 1

print(f"{search_for} appeared {count} times")


