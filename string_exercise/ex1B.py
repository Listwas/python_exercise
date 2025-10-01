#Create a string made of the middle three characters

def get_middle(str1):
    print("original string:", str1)

    middle = int(len(str1) // 2)
    print("middle three characters:", str1[middle - 1:middle + 2] )


get_middle("JohnDipPeta")
get_middle("JaSonAy")


