# Modifies global variable
#Define a global variable global_var = 10. Write a function that modifies a global variable value.
global_var = 10

def modify_global(new_value):
    global global_var
    global_var = new_value

print(global_var)
modify_global(11)
print(global_var)
