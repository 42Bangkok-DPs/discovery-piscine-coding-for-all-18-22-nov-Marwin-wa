num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = num1 * num2

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print("The result of multiplying {} and {} is: {}".format(num1, num2, result))