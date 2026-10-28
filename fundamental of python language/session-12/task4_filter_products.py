# ==============================================================================
# Task 4: Filter Products Starting with 'M' Using filter() and lambda
# File: session-11/task4_filter_products.py
# Purpose: Filter products starting with letter 'M' using filter() and lambda.
# ==============================================================================

products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

# filter(function, list) keeps only the items where the function returns True
# lambda item: item.startswith('M') checks if the first letter is 'M'
m_products = list(filter(lambda item: item.startswith('M'), products))

print("All Products :", products)
print("Products starting with 'M':", m_products)

