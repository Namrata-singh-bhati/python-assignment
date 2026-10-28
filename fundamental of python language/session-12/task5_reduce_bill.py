# ==============================================================================
# Task 5: Calculate Swiggy Bill Using reduce() and lambda
# File: session-11/task5_reduce_bill.py
# Purpose: Calculate total bill amount using reduce() and a lambda function.
# Hint: Import reduce from functools.
# ==============================================================================

# 1. Import reduce from the built-in functools module
from functools import reduce

# 2. List of item prices in a Swiggy order
item_prices = [120, 80, 150, 60]

# 3. reduce(function, list) combines elements from left to right
# lambda total, price: total + price adds each price to the running total
total_bill = reduce(lambda total, price: total + price, item_prices)

print("Swiggy Item Prices :", item_prices)
print("Total Bill Amount  : ₹", total_bill)

