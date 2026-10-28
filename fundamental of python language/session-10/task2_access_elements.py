# ==============================================================================
# Task 2: Access Tuple Elements Using Indexing
# File: session-9/task2_access_elements.py
# Purpose: Access and print the 2nd and 4th app names from fav_apps tuple.
# ==============================================================================

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

# In Python, indexing starts at 0:
# - Index 0 = 1st element ('Instagram')
# - Index 1 = 2nd element ('Zomato')
# - Index 2 = 3rd element ('Spotify')
# - Index 3 = 4th element ('WhatsApp')
# - Index 4 = 5th element ('Flipkart')

second_app = fav_apps[1]
fourth_app = fav_apps[3]

print("Full Tuple:", fav_apps)
print("2nd App (Index 1):", second_app)
print("4th App (Index 3):", fourth_app)

