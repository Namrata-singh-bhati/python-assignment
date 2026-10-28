# ==============================================================================
# Task 3: Zomato-Style Bill Calculator
# File: session-3/task3_zomato_bill.py
# Purpose: Take item price (float) and quantity (int), calculate total bill,
#          and display it in a friendly currency format.
# ==============================================================================

# 1. Ask for the food item price (converted to float for decimal values like 175.25)
price = float(input("Enter the price of the food item (₹): "))

# 2. Ask for the quantity (converted to int because quantity is a whole number like 2)
quantity = int(input("Enter the quantity: "))

# 3. Calculate total bill
total_bill = price * quantity

# 4. Display the total bill (:.2f formats the decimal to 2 decimal places)
print(f"Your total bill is ₹{total_bill:.2f}")

