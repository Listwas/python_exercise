#Create a function with variable length of arguments

def func1(*args):
    for arg in args:
        print(arg)

func1(20, 30, 40)
