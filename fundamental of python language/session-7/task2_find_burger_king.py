# ==============================================================================
# Task 2: Stop at 'Burger King' Using break
# File: session-6/task2_find_burger_king.py
# Purpose: Loop through food items and break when 'Burger King' is found.
# ==============================================================================

# What does 'break' do?
# 'break' stops the entire loop completely and immediately exits.

foods = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

print("Searching through foods:")

for item in foods:
    # If we find 'Burger King', print the message and break out of the loop
    if item == 'Burger King':
        print("Found Burger King, stopping search.")
        break
    
    # Print the current food item
    print(item)

