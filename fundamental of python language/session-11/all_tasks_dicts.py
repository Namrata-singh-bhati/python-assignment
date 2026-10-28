# ==============================================================================
# Complete Session 10: All Dictionary Tasks
# File: session-10/all_tasks_dicts.py
# Purpose: Step-by-step demonstration of dictionary creation, modification,
#          iteration, keys(), values(), items(), and cart update function.
# ==============================================================================

print("=" * 60)
print("            PYTHON DICTIONARY OPERATIONS")
print("=" * 60)

# Task 1: Create my_playlist
my_playlist = {
    'Blinding Lights': 3.20,
    'Shape of You': 3.53,
    'Levitating': 3.23
}
print("\n[Task 1] Created Playlist Dictionary:")
print(my_playlist)

# Task 2: Add and update
my_playlist['Stay'] = 2.21
my_playlist['Blinding Lights'] = 3.35
print("\n[Task 2] After Adding 'Stay' and Updating 'Blinding Lights':")
print(my_playlist)

# Task 3: display_friends function
def display_friends(friends):
    for user, followers in friends.items():
        print(f"   {user}: {followers} followers")

instagram_friends = {'priya_travels': '2.3K', 'rahul_music': '15.8K'}
print("\n[Task 3] display_friends() Output:")
display_friends(instagram_friends)

# Task 4: keys(), values(), items()
food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}
print("\n[Task 4] Dictionary Methods on food_order:")
print("   All food items (keys):", list(food_order.keys()))
print("   All quantities (values):", list(food_order.values()))
print("   Items & Quantities (items):")
for item, qty in food_order.items():
    print(f"     - {item}: {qty}")

# Task 5: update_cart function
def update_cart(cart, item, qty):
    cart[item] = qty
    return cart

cart = {'T-Shirt': 1}
print("\n[Task 5] update_cart() Output:")
print("   Initial Cart:", cart)
update_cart(cart, 'Jeans', 2)
print("   After Adding 'Jeans':", cart)
update_cart(cart, 'T-Shirt', 3)
print("   After Updating 'T-Shirt':", cart)

print("\n" + "=" * 60)

