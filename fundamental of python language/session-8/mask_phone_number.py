# ==============================================================================
# Task 5: Mask Phone Number Function
# File: session-7/mask_phone_number.py
# Purpose: Create a function mask_phone_number(phone) that returns '******1234'.
# Hint: Use string slicing and concatenation (+).
# ==============================================================================

def mask_phone_number(phone):
    # 1. String slicing: [-4:] extracts the last 4 digits
    last_four = phone[-4:]
    
    # 2. String concatenation: join '******' with the last 4 digits
    masked = "******" + last_four
    
    return masked

# --- Testing the function ---
if __name__ == "__main__":
    sample_phone1 = "9876541234"
    sample_phone2 = "9123456789"
    
    print("Original Phone 1:", sample_phone1)
    print("Masked Phone 1  :", mask_phone_number(sample_phone1))
    print()
    print("Original Phone 2:", sample_phone2)
    print("Masked Phone 2  :", mask_phone_number(sample_phone2))

