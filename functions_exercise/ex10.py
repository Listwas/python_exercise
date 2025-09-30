#Call Function using both positional and keyword arguments

def describe_pet(animal_type, pet_name):
    print(animal_type, pet_name)

#positional 
describe_pet("cat", "ben")
describe_pet("dog", "gek")

#keyword
describe_pet(animal_type="cat", pet_name="ben")
describe_pet(animal_type="dog", pet_name="gek")
