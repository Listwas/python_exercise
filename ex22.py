#Capitalize the first letter of each word in a string


def capitalize_words(string):
    words = string.split()
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    return " ".join(capitalized)

user_sentence = input("your sentence to capitalize: ")
print(capitalize_words(user_sentence))

