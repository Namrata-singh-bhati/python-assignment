# ==============================================================================
# Task 1: Instagram Caption First 10 Characters
# File: session-7/insta_caption.py
# Purpose: Take an Instagram caption as input and print the first 10 characters
#          using string indexing / slicing.
# ==============================================================================

# 1. Ask user for an Instagram caption
caption = input("Enter your Instagram caption: ")

# 2. In Python, string indices start at 0.
# Slicing [0:10] extracts characters starting from index 0 up to index 9
# (which gives us the first 10 characters).
first_10_chars = caption[0:10]

# 3. Print the result
print("Original Caption:", caption)
print("First 10 Characters:", first_10_chars)

