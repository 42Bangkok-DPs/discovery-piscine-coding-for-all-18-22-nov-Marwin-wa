import math

user_input = input("Give me a number: ")

try:
    num = float(user_input)
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    print("That's not a valid number.")

