def display_menu():
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    print("Hello! Welcome!")

def check_even_odd():
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num % 2 == 0:
                print(f"{num} is an Even number.")
            else:
                print(f"{num} is an Odd number.")
            break  
        except ValueError:
            print("Error: Please enter a valid integer.")

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
    elif choice == 2:
        check_even_odd()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
    return False  

def main():
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(user_choice):
                break  
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()