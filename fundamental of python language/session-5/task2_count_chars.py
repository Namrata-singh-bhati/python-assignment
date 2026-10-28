# ==============================================================================
# Task 2: Count Characters Excluding Spaces
# File: session-4/task2_count_chars.py
# Purpose: Use a for loop and an if statement to count non-space characters.
# ==============================================================================

# 1. Given user bio
user_bio = 'Music lover | Foodie | Traveller'

# 2. Counter variable starting at 0
character_count = 0

# 3. Loop through every character in the bio string
for char in user_bio:
    # If the current character is NOT a space, increase our counter by 1
    if char != " ":
        character_count = character_count + 1

# 4. Display the result
print("User Bio:", user_bio)
print("Total characters (excluding spaces):", character_count)

