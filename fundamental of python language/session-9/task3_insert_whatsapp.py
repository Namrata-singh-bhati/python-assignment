# ==============================================================================
# Task 3: Insert 'WhatsApp' at the Second Position
# File: session-8/task3_insert_whatsapp.py
# Purpose: Insert 'WhatsApp' at index 1 using insert() and print the result.
# Hint: List indices start from 0 (index 0 = 1st, index 1 = 2nd position).
# ==============================================================================

my_fav_apps = ['Instagram', 'Zomato', 'Spotify', 'YouTube', 'Flipkart', 'Netflix']

# insert(index, item) puts the item at that exact index and shifts others right
my_fav_apps.insert(1, 'WhatsApp')

print("List after inserting 'WhatsApp' at the 2nd position (index 1):")
print(my_fav_apps)

