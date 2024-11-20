
number = int(input("Enter a number to display its multiplication table: "))


print(f"Multiplication Table for {number}:")
for i in range(1, 11): 
    print(f"{number} x {i} = {number * i}")
