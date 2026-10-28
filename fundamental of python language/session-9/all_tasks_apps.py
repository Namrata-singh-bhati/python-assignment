# ==============================================================================
# Complete Session 8: All Tasks on my_fav_apps List
# File: session-8/all_tasks_apps.py
# Purpose: Step-by-step demonstration of append(), insert(), remove(), pop(),
#          sort(), and reverse() on my_fav_apps.
# ==============================================================================

print("=" * 60)
print("       STEP-BY-STEP LIST OPERATIONS: my_fav_apps")
print("=" * 60)

# Task 1: Create initial list
my_fav_apps = ['Instagram', 'Zomato', 'Spotify', 'YouTube', 'Flipkart']
print("\n[Step 1] Initial List:")
print(my_fav_apps)

# Task 2: Append a new app
my_fav_apps.append('Netflix')
print("\n[Step 2] After append('Netflix'):")
print(my_fav_apps)

# Task 3: Insert 'WhatsApp' at 2nd position (index 1)
my_fav_apps.insert(1, 'WhatsApp')
print("\n[Step 3] After insert(1, 'WhatsApp'):")
print(my_fav_apps)

# Task 4: Remove 'Flipkart' and pop the last app
my_fav_apps.remove('Flipkart')
print("\n[Step 4a] After remove('Flipkart'):")
print(my_fav_apps)

last_app = my_fav_apps.pop()
print(f"\n[Step 4b] After pop() (removed '{last_app}'):")
print(my_fav_apps)

# Task 5: Sort alphabetically, then reverse order
my_fav_apps.sort()
print("\n[Step 5a] Alphabetical order using sort():")
print(my_fav_apps)

my_fav_apps.reverse()
print("\n[Step 5b] Reversed order using reverse():")
print(my_fav_apps)

print("\n" + "=" * 60)

