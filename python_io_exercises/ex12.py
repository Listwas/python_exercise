#Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action

def main():
    quit = 0
    while quit == 0:
        print("1.say hello 2.calculate square 3.exit")
        option = int(input("select option: "))

        match option:
            case 1:
                print("hello")
            case 2:
                res = int(input("number: ")) ** int(input("power: "))
                print("result:",res)
            case 3:
                quit = 1
            case _:
                print("invalid option")
                            
main()


