# ==============================================================================
# Task 1: Instagram Account Age Eligibility
# File: session-4/task1_instagram_age.py
# Purpose: Check if user is 13 or older to create an Instagram account.
# ==============================================================================

# 1. Ask user for their age and convert to an integer
age = int(input("Enter your age: "))

# 2. Check if age is 13 or older using if and else
if age >= 13:
    print("Eligible to create an account on Instagram.")
else:
    print("Not eligible. You must be 13 or older to create an Instagram account.")

