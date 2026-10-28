# ==============================================================================
# Task 3: Zomato Late-Night Food Order Check
# File: session-4/task3_zomato_late_night.py
# Purpose: Check if age >= 18 and time is between 22 (10pm) and 2 (2am).
# Constraint: Use nested if statements.
# Hint: Handle midnight crossover with: time >= 22 or time <= 2.
# ==============================================================================

# 1. Take age and time (24-hour format)
age = int(input("Enter your age: "))
current_time = int(input("Enter current time in 24-hour format (0-23): "))

# 2. Outer if: checks if age is 18 or above
if age >= 18:
    # Inner if (nested): checks if time is between 22 (10 PM) and 2 (2 AM)
    if current_time >= 22 or current_time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")

