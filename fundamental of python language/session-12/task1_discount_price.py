# ==============================================================================
# Task 1: Calculate Discounted Price Function
# File: session-11/task1_discount_price.py
# Purpose: Define get_discounted_price(price, discount_percent) and test it.
# ==============================================================================

def get_discounted_price(price, discount_percent):
    # Calculate discount amount: (price * discount_percent) / 100
    discount_amount = price * (discount_percent / 100)
    
    # Final price after subtracting discount
    final_price = price - discount_amount
    return final_price

# --- Testing the function ---
if __name__ == "__main__":
    original_price = 500
    discount = 10
    
    result = get_discounted_price(original_price, discount)
    print(f"Original Price : ₹{original_price}")
    print(f"Discount       : {discount}%")
    print(f"Final Price    : ₹{result}")

