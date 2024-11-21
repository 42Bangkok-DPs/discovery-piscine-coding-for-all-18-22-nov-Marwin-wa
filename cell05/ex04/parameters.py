import sys
user_input = input("Enter some parameters (separated by spaces): ")

user_parameters = user_input.split()

num_params = len(user_parameters)

print(f"Number of parameters: {num_params}.")
