# ==============================================================================
# Task 3: Convert Song Durations Using map() and lambda
# File: session-11/task3_map_durations.py
# Purpose: Convert minutes to seconds using map() and a lambda function.
# ==============================================================================

# Song durations in minutes
durations_in_minutes = [3.5, 4.0, 2.5, 5.0, 1.5]

# map(function, list) applies the function to each item in the list
# lambda minutes: int(minutes * 60) multiplies each minute value by 60
durations_in_seconds = list(map(lambda mins: int(mins * 60), durations_in_minutes))

print("Song Durations in Minutes :", durations_in_minutes)
print("Song Durations in Seconds :", durations_in_seconds)

