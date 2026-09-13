def print_menu():
    print("1. About me")
    print("2. My goals")
    print("3. Exit")
    print("4. Founding day")

def about_me(name):
    return f"my name is {name}"
run = True
print("Welcome to the Launch Console!")
name = input("Whats your name? ")
print(f"Hi {name}!")
while run:
    print_menu()
    choice = input("Please select an option: ")
    if choice == "1":
        print(about_me("Mason"))
    elif choice == "2":
        print(f"My goals are to have fun and learn new things!")
    elif choice == "3":
        print("Exiting the console. Goodbye!")
        run = False
    elif choice == "4":
        print("Grade")
    else:
        print("Invalid option. Please try again.")



