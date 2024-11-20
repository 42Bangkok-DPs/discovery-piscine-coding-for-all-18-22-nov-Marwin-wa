

def main():
    # Set the correct password
    correct_password = "PythonSoHard"
    
    # Prompt the user to enter a password
    entered_password = input("Enter the password: ")
    
    # Check if the entered password matches the correct password
    if entered_password == correct_password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()
