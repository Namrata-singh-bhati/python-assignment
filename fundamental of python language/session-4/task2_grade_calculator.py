# ==============================================================================
# Task 2: Student Grade Calculator
# File: session-4/task2_grade_calculator.py
# Purpose: Ask for marks (0-100) and print grade:
#          90+ = 'A', 75-89 = 'B', 60-74 = 'C', 40-59 = 'D', below 40 = 'F'.
# ==============================================================================

# 1. Ask user for marks (0-100)
marks = float(input("Enter your marks (0-100): "))

# 2. Check grade using if, elif, else
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

