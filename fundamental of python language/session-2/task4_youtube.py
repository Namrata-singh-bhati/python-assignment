# ==============================================================================
# Task 4: Primitive vs Non-Primitive Data Types for YouTube Video
# File: session-2/task4_youtube.py
# Purpose: Identify primitive vs non-primitive types and explain with comments.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Variable Declarations
# ------------------------------------------------------------------------------
title = "Python Tutorial for Absolute Beginners"  # Type: str (String)
views = 250000                                    # Type: int (Integer)
likes = 15000                                     # Type: int (Integer)
is_premium = False                                # Type: bool (Boolean)


# ------------------------------------------------------------------------------
# 2. What are Primitive vs Non-Primitive Data Types?
# ------------------------------------------------------------------------------
# PRIMITIVE DATA TYPES:
# - These are the most basic, fundamental data types in programming.
# - They hold a single, simple value at a time (like a single number or True/False).
# - Examples: int (integer), float (decimal), bool (boolean).
#
# NON-PRIMITIVE DATA TYPES:
# - These are complex data types that can hold multiple values or collections of items.
# - In general computer science, a String (str) is considered NON-PRIMITIVE because
#   it is not a single value; it is a sequence/collection of individual characters 
#   grouped together (e.g. 'P', 'y', 't', 'h', 'o', 'n').
# - Other non-primitive types in Python include: list, dict, set, and tuple.


# ------------------------------------------------------------------------------
# 3. Classification of the YouTube Variables:
# ------------------------------------------------------------------------------
#
# 1. views = 250000
#    - Data Type: int (Integer)
#    - Category: PRIMITIVE
#    - Reason: It stores only one single whole number value.
#
# 2. likes = 15000
#    - Data Type: int (Integer)
#    - Category: PRIMITIVE
#    - Reason: It stores only one single whole number value.
#
# 3. is_premium = False
#    - Data Type: bool (Boolean)
#    - Category: PRIMITIVE
#    - Reason: It stores only a single True or False condition.
#
# 4. title = "Python Tutorial for Absolute Beginners"
#    - Data Type: str (String)
#    - Category: NON-PRIMITIVE (in general programming / computer science)
#    - Reason: A string is a sequence (collection) of multiple characters joined 
#      together. (Note: in basic Python, strings are often introduced alongside 
#      primitive types, but structurally they are collection/sequence types).


# ------------------------------------------------------------------------------
# 4. Displaying the Details in Terminal
# ------------------------------------------------------------------------------
print("==================================================================")
print("     YOUTUBE VIDEO VARIABLES & DATA TYPE CLASSIFICATION")
print("==================================================================")

print("1. Variable: views")
print("   - Value       :", views)
print("   - Type        :", type(views))
print("   - Category    : PRIMITIVE (stores a single integer)")
print()

print("2. Variable: likes")
print("   - Value       :", likes)
print("   - Type        :", type(likes))
print("   - Category    : PRIMITIVE (stores a single integer)")
print()

print("3. Variable: is_premium")
print("   - Value       :", is_premium)
print("   - Type        :", type(is_premium))
print("   - Category    : PRIMITIVE (stores a single boolean True/False)")
print()

print("4. Variable: title")
print("   - Value       :", title)
print("   - Type        :", type(title))
print("   - Category    : NON-PRIMITIVE (sequence of individual characters)")
print("==================================================================")

