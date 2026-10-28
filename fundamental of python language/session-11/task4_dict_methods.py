# ==============================================================================
# Task 4: Dictionary Methods: keys(), values(), items()
# File: session-10/task4_dict_methods.py
# Purpose: Given food_order, print:
#          a) all food items using keys()
#          b) all quantities using values()
#          c) each item with its quantity using items()
# ==============================================================================

food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

print("Original food_order Dictionary:")
print(food_order)
print("=" * 50)

# a) All food items using keys()
print("a) All Food Items (keys):")
for item in food_order.keys():
    print(f"   - {item}")
print()

# b) All quantities using values()
print("b) All Quantities (values):")
for qty in food_order.values():
    print(f"   - {qty}")
print()

# c) Each item with its quantity using items()
print("c) Each Item with Quantity (items):")
for item, qty in food_order.items():
    print(f"   - {item}: {qty}")
print("=" * 50)

