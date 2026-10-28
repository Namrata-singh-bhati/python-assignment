# ==============================================================================
# Task 4: Simulate Loading Spinner with while True and break
# File: session-5/task4_loading_spinner.py
# ==============================================================================

count = 0

while True:
    print("Loading...")
    count = count + 1
    if count == 3:
        break

print("Done loading!")

