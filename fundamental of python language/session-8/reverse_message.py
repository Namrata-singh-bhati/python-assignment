# ==============================================================================
# Task 3: Reverse Message Function
# File: session-7/reverse_message.py
# Purpose: Reverse any string passed to reverse_message(message).
# Constraint: Do not use built-in reversed() or [::-1] slicing shortcut.
# ==============================================================================

def reverse_message(message):
    # Start with an empty string
    reversed_str = ""
    
    # Loop through each character in the message
    # Adding the new character to the FRONT reverses the order!
    for char in message:
        reversed_str = char + reversed_str
        
    return reversed_str

# --- Testing the function ---
if __name__ == "__main__":
    test_msg1 = "Hello WhatsApp"
    test_msg2 = "Python"
    
    print("Original:", test_msg1)
    print("Reversed:", reverse_message(test_msg1))
    print()
    print("Original:", test_msg2)
    print("Reversed:", reverse_message(test_msg2))

