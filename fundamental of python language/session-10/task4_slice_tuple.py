# ==============================================================================
# Task 4: Tuple Slicing (Middle Three Apps)
# File: session-9/task4_slice_tuple.py
# Purpose: Use tuple[start:end] slicing syntax to select the middle three elements.
# ==============================================================================

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
# Indices:      0           1          2           3           4

# The middle three elements are at indices 1, 2, and 3:
# ('Zomato', 'Spotify', 'WhatsApp')
#
# Slicing syntax: tuple[start:end]
# Note: 'end' is excluded in Python slicing, so we slice from 1 to 4:
middle_three = fav_apps[1:4]

print("Full Tuple         :", fav_apps)
print("Middle Three Apps  :", middle_three)

