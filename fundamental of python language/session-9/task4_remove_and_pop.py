# ==============================================================================
# Task 4: Remove and Pop Items from List
# File: session-8/task4_remove_and_pop.py
# Purpose: Remove an app using remove(), then remove the last app using pop(),
#          printing the list after each operation.
# ==============================================================================

my_fav_apps = ['Instagram', 'WhatsApp', 'Zomato', 'Spotify', 'YouTube', 'Flipkart', 'Netflix']

# 1. remove() finds and removes an item by its exact value
my_fav_apps.remove('Flipkart')
print("1. After removing 'Flipkart' using remove():")
print(my_fav_apps)

# 2. pop() removes the last item from the list
removed_app = my_fav_apps.pop()
print(f"\n2. After removing the last app ('{removed_app}') using pop():")
print(my_fav_apps)

