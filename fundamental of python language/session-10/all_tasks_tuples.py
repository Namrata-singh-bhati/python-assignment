# ==============================================================================
# Complete Session 9: All Tuple Tasks
# File: session-9/all_tasks_tuples.py
# Purpose: Step-by-step demonstration of tuple creation, indexing, immutability,
#          slicing, and concatenation.
# ==============================================================================

print("=" * 60)
print("             PYTHON TUPLE OPERATIONS")
print("=" * 60)

# Task 1: Create tuple
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
print("\n[Task 1] Created Tuple:")
print(fav_apps)

# Task 2: Access 2nd and 4th elements
print("\n[Task 2] Access Elements via Indexing:")
print("2nd App (Index 1):", fav_apps[1])
print("4th App (Index 3):", fav_apps[3])

# Task 3: Immutability check
print("\n[Task 3] Tuple Immutability Check:")
try:
    fav_apps[0] = 'YouTube'
except TypeError as e:
    print("Caught Expected Error:", e)
    print("Explanation: Tuples are immutable; items cannot be reassigned!")

# Task 4: Slicing middle three elements
print("\n[Task 4] Slicing Middle Three Elements [1:4]:")
print("Middle Three:", fav_apps[1:4])

# Task 5: Concatenating tuples
new_apps = ('Netflix', 'Amazon')
all_apps = fav_apps + new_apps
print("\n[Task 5] Concatenation with new_apps:")
print("All Apps Combined:", all_apps)

print("\n" + "=" * 60)

