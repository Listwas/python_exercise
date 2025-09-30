#Create a function with a default argument

def show_employee(name, salary=9000):
    return name, salary

print(show_employee("Ben", 12000))
print(show_employee("Jessa"))
