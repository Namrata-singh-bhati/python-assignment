# ==============================================================================
# Complete Session 11: Functions, Lambda, Map, Filter, and Reduce
# File: session-11/all_tasks_functions.py
# Purpose: Step-by-step demonstration of functions, lambda, map, filter, and reduce.
# ==============================================================================

from functools import reduce

print("=" * 60)
print("     PYTHON FUNCTIONS, LAMBDA, MAP, FILTER, REDUCE")
print("=" * 60)

# Task 1: get_discounted_price
def get_discounted_price(price, discount_percent):
    return price - (price * (discount_percent / 100))

print("\n[Task 1] get_discounted_price(500, 10):")
print("   Final Price: ₹", get_discounted_price(500, 10))

# Task 2: format_follower_count
def format_follower_count(count):
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    elif count >= 1_000:
        return f"{count / 1_000:.1f}K"
    else:
        return str(count)

print("\n[Task 2] format_follower_count:")
print("   1500     ->", format_follower_count(1500))
print("   1200000  ->", format_follower_count(1200000))

# Task 3: map() with lambda
durations_mins = [3.5, 4.0, 2.5]
durations_secs = list(map(lambda m: int(m * 60), durations_mins))
print("\n[Task 3] map() with lambda (Minutes to Seconds):")
print(f"   {durations_mins} -> {durations_secs}")

# Task 4: filter() with lambda
products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']
m_products = list(filter(lambda item: item.startswith('M'), products))
print("\n[Task 4] filter() with lambda (Products starting with 'M'):")
print(f"   Filtered: {m_products}")

# Task 5: reduce() with lambda
prices = [120, 80, 150, 60]
total = reduce(lambda acc, p: acc + p, prices)
print("\n[Task 5] reduce() with lambda (Total Swiggy Bill):")
print(f"   Prices {prices} -> Total: ₹{total}")

print("\n" + "=" * 60)

