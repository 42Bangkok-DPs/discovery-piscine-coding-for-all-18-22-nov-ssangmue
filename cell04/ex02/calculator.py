num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# To avoid division by zero error, check if num2 is not zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"

# Display the results
print(f"The sum of {num1} and {num2} is: {addition}")
print(f"The difference between {num1} and {num2} is: {subtraction}")
print(f"The product of {num1} and {num2} is: {multiplication}")
print(f"The division of {num1} by {num2} is: {division}")