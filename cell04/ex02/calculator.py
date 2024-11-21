#!/usr/bin/env python3


num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))


print("Thank you!")


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"


print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplication}")
