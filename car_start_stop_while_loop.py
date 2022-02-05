command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
Start - to start the car.
Stop - to stop the car.
Quit - to exit. 
""")
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("The car has already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
        break
else:
    print("Sorry! I don't understand that...")














