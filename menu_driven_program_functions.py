def display_menu():
    """
    Displays the menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")

def check_even_odd(number: int) -> str:
    """
    Determines if the given number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.  
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def even_odd_checker_action():
    """
    Handles the logic for getting user input and checking if the number is even or odd.
    """
    try:
        number = int(input("Enter an integer: "))
        result = check_even_odd(number)
        print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.
    
    Args:
        choice (int): The menu option selected by the user.
    
    Returns:
        bool: Returns True if the program should exit, False otherwise.
    """
    if choice == 1:
        greet_user()
        return False
    elif choice == 2:
        even_odd_checker_action()
        return False
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice! Please enter a valid option (1-3).")
        return False

def main():
    """
    Main function that controls the flow of the menu-driven program.
    """
    while True:
        display_menu()
        try:
            # Get the user's menu choice
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 3.")
            continue
        
        # Handle the user's menu choice
        if handle_menu_choice(choice):
            break  # Exit the loop if the user selects 'Exit'

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
