# James Sargent
# 06/2024
# Assignment Name: Introduction to Python 3
# A brief description of the project:
#   This program prompts the user to enter their first name and last name separately,
#   and then displays a personalized welcome message to the user.

def main():
    # Prompt the user to enter their first name
    first_name = input("Enter your first name: ")
    
    # Prompt the user to enter their last name
    last_name = input("Enter your last name: ")
    
    # Print a welcome message including the user's full name
    print(f"Welcome to this course, {first_name} {last_name}!")

# Entry point of the program
if __name__ == "__main__":
    main()
