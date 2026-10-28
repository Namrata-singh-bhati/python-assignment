# ==============================================================================
# Task 3: Right-Angled Triangle Pattern Using a while Loop
# File: session-5/task3_triangle_pattern.py
# ==============================================================================

row = 1

while row <= 5:
    star = 1
    while star <= row:
        print("*", end="")
        star = star + 1
    print()
    row = row + 1

