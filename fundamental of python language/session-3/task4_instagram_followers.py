# ==============================================================================
# Task 4: Instagram Follower Count with Escape Characters
# File: session-3/task4_instagram_followers.py
# Purpose: Ask for follower count, convert to int, and print with \n and \t.
# ==============================================================================

# 1. Ask for Instagram follower count and convert to int
followers = int(input("Enter your Instagram follower count: "))

# 2. Print using escape characters:
#    '\n' adds a new empty line (Enter key)
#    '\t' adds a tab space (indent)
#    '{followers:,}' adds commas to numbers (e.g., 1500 becomes 1,500)
print(f"\n\tYou have {followers:,} followers")

