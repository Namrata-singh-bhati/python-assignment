# ==============================================================================
# Task 2: Arithmetic Operations with Two Numbers
# File: session-3/task2_arithmetic.py
# Purpose: Take two numbers as input, convert to integers, and calculate:
#          Sum (+), Difference (-), Product (*), and Quotient (/).
# ==============================================================================

# Beginner Note:
# input() always captures what the user types as text (a string).
# We must use int() to convert that text into a real number before doing math!

# 1. Take inputs and convert to integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# 2. Perform the arithmetic calculations
sum_result = num1 + num2        # Sum (Addition)
diff_result = num1 - num2       # Difference (Subtraction)
prod_result = num1 * num2       # Product (Multiplication)
quot_result = num1 / num2       # Quotient (Division)

# 3. Print the results
print("\n--- Arithmetic Results ---")
print("Sum        :", sum_result)
print("Difference :", diff_result)
print("Product    :", prod_result)
print("Quotient   :", quot_result)

