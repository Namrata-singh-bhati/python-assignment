# ==============================================================================
# Task 4: Flipkart Product Description Analysis
# File: session-7/flipkart_words.py
# Purpose: Extract first word, last word, and total words using:
#          - split()
#          - indexing
#          - len()
# ==============================================================================

# Sample Flipkart product description
description = "Fast charging wireless Bluetooth headphones with deep bass sound"

# 1. Use split() to break the description into a list of words
words = description.split()

# 2. Use indexing to get the first word (index 0) and last word (index -1)
first_word = words[0]
last_word = words[-1]

# 3. Use len() to count the total number of words
total_words = len(words)

# Display the results
print("Product Description:", description)
print("-" * 50)
print("First Word        :", first_word)
print("Last Word         :", last_word)
print("Total Words Count :", total_words)

