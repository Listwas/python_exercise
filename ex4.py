#Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word, n):
    if len(word) > n:
        return word[n:]
    else:
        return "string was too small for your n"

print("Removing characters from a string")
s = input("string: ")
n = int(input("n: "))

print(remove_chars(s, n))
