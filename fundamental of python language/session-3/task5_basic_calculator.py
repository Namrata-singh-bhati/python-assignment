# ==============================================================================
# Task 5: Basic Calculator Program
# File: session-3/task5_basic_calculator.py
# Purpose: Take two numbers and an operator (+, -, *, /), calculate the result,
#          and handle invalid operators with an error message.
# ==============================================================================

# 1. Ask the user for the two numbers and convert them using float() (typecasting)
# float() allows both whole numbers (like 10) and decimal numbers (like 2.5)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Ask the user to choose an operator
operator = input("Enter an operator (+, -, *, /): ")

# 3. Check the operator using simple if-elif-else statements
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    # Prevent division by zero error
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    # Error message if the user enters something other than +, -, *, /
    print(f"Error: Invalid operator '{operator}'. Please use +, -, *, or /.")

