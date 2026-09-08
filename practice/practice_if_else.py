car = False
while True:
    command = input("Enter a command: ")
    if command == "start":
        if car:
            print("car already startrd")
        else:
            car = True
            print("car started")
    elif command == "stop":
        if car != True:
            print("Start the car first")
        else:
            car = False
            print("car stopped")
    elif command == "help":
        print("""
        >start - start the car
        >stop - stop the car
        >help - see the instructions
        """)
    elif command == "quit":
        break
    else:
        print("Command not reconised")
