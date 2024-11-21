age_string = input("Please tell me your age: ")
try:
    age = int(age_string)  
    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {age + 10} years old.")
    print(f"In 20 years, you'll be {age + 20} years old.")
    print(f"In 30 years, you'll be {age + 30} years old.")
except ValueError:
    print("That's not a valid number!")