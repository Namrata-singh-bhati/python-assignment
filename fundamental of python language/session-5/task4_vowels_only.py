# ==============================================================================
# Task 4: Print Vowels Only from User Input
# File: session-4/task4_vowels_only.py
# Purpose: Ask the user for a word and print each vowel on a new line.
# Constraint: Do not use the 'in' operator inside the if statement.
#             Use multiple '==' checks instead.
# ==============================================================================

# 1. Ask the user for a word or song name
word = input("Enter a word or song name: ")

print("\nVowels in your word:")

# 2. Loop through every character in the word
for char in word:
    # Check for both lowercase and uppercase vowels using multiple '==' checks
    # (Notice: no 'in' operator is used here!)
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
       char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print(char)
