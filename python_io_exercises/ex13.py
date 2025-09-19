#Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.

word = input("word: ")
number = int(input("number: "))
print(f"{word:>20}{number}")

