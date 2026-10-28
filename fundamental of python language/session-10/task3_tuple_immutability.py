# ==============================================================================
# Task 3: Tuple Immutability and Error Observation
# File: session-9/task3_tuple_immutability.py
# Purpose: Try to modify a tuple element, observe the error, and explain why.
# ==============================================================================

# ------------------------------------------------------------------------------
# WHY DOES THIS ERROR HAPPEN? (Explanation of Tuple Immutability)
# ------------------------------------------------------------------------------
# In Python, Tuples are IMMUTABLE.
# "Immutable" means once a tuple is created, its values CANNOT be changed,
# modified, added, or deleted.
#
# If you try to do: fav_apps[0] = 'YouTube'
# Python raises a: TypeError: 'tuple' object does not support item assignment
#
# Unlike Lists (which are MUTABLE and can be changed anytime), Tuples are
# designed to protect data from accidental modification.
# ------------------------------------------------------------------------------

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("Original Tuple:", fav_apps)
print("Attempting to change fav_apps[0] to 'YouTube'...\n")

# We use a try-except block so the program demonstrates the error without crashing
try:
    fav_apps[0] = 'YouTube'
except TypeError as error:
    print("Caught Expected Error:")
    print("Error Type   :", type(error).__name__)
    print("Error Message:", error)
    print("\nConclusion: Tuples cannot be modified after creation because they are immutable!")

