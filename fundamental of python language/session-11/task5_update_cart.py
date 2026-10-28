# ==============================================================================
# Task 5: Flipkart-Style Cart Update Function
# File: session-10/task5_update_cart.py
# Purpose: Write update_cart(cart, item, qty) to add or update items in cart.
# Hint: Use direct assignment or update() method.
# ==============================================================================

def update_cart(cart, item, qty):
    # Direct assignment cart[item] = qty (or cart.update({item: qty}))
    # Automatically adds the item if it's new, or updates quantity if it already exists!
    cart[item] = qty
    return cart

# --- Testing the function ---
if __name__ == "__main__":
    my_cart = {
        'Wireless Mouse': 1,
        'Bluetooth Headphones': 1
    }
    
    print("Initial Cart:")
    print(my_cart)
    
    # 1. Adding a new item to cart
    update_cart(my_cart, 'USB-C Cable', 2)
    print("\nAfter adding new item ('USB-C Cable', qty: 2):")
    print(my_cart)
    
    # 2. Updating quantity of an existing item
    update_cart(my_cart, 'Wireless Mouse', 3)
    print("\nAfter updating existing item ('Wireless Mouse', qty: 3):")
    print(my_cart)

