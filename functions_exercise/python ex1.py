#Write a program to create a function that takes two arguments, name and age, and prints their values.

def test(name, age):
    return f"hello {name}, your age is {age}"

name = input("your name: ")
age = int(input("your age: "))

print(test(name, age))

