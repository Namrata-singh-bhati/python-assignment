# ==============================================================================
# Task 5: Pyramid Star Pattern Using Nested while Loops
# File: session-5/task5_pyramid_pattern.py
# Purpose: Print a 4-row pyramid pattern using two nested while loops.
# ==============================================================================

total_rows = 4
row = 1

while row <= total_rows:
    # 1. First nested while loop: leading spaces
    spaces = total_rows - row
    s = 1
    while s <= spaces:
        print(" ", end="")
        s = s + 1
        
    # 2. Second nested while loop: stars (1, 3, 5, 7)
    stars = (2 * row) - 1
    k = 1
    while k <= stars:
        print("*", end="")
        k = k + 1
        
    print()
    row = row + 1

