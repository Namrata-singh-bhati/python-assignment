# ==============================================================================
# Task 4: Filter Spam with continue and Stop with break
# File: session-6/task4_filter_spam.py
# Purpose: Print non-spam messages by skipping 'Spam' using continue,
#          and stop reading if 'How are you?' is found using break.
# ==============================================================================

# Hint applied: Using both 'continue' and 'break' inside the same loop.

messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

print("Reading messages:")

for msg in messages:
    # 1. Skip any message that is 'Spam' using continue
    if msg == 'Spam':
        continue
    
    # 2. Stop reading completely if 'How are you?' is found using break
    if msg == 'How are you?':
        print("Found 'How are you?' - stopping reading further.")
        break
    
    # 3. Print the valid, non-spam message
    print(msg)

