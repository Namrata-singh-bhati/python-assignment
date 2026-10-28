# ==============================================================================
# Task 2: Zomato Offer Countdown Using a while Loop
# File: session-5/task2_zomato_countdown.py
# Purpose: Start with minutes_left = 5 and count down until it reaches 0.
# ==============================================================================

# Start with 5 minutes left
minutes_left = 5

# while loop continues until minutes_left reaches 0
while minutes_left >= 0:
    print(f"Offer ends in {minutes_left} minutes")
    # Decrease minutes_left by 1 after each print
    minutes_left = minutes_left - 1
