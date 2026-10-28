# ==============================================================================
# Task 1: Skip 'Banana' Using continue
# File: session-6/task1_skip_banana.py
# Purpose: Loop through fruits and skip 'Banana' using the continue statement.
# ==============================================================================

# What does 'continue' do?
# 'continue' tells Python to skip the rest of the current loop step
# and jump directly to the next item in the list.

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

print("List of fruits (skipping Banana):")

for fruit in fruits:
    # If the fruit is 'Banana', skip it!
    if fruit == 'Banana':
        continue
    
    # This print will only run for fruits that are NOT Banana
    print(fruit)

