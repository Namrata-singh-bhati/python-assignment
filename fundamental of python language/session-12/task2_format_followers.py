# ==============================================================================
# Task 2: Format Follower Count (Instagram Style)
# File: session-11/task2_format_followers.py
# Purpose: Define format_follower_count(count) to format 1500 as '1.5K',
#          1200000 as '1.2M', etc.
# Hint: Use if-elif-else to check number ranges.
# ==============================================================================

def format_follower_count(count):
    # 1. Millions (1,000,000 and above)
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    
    # 2. Thousands (1,000 to 999,999)
    elif count >= 1_000:
        return f"{count / 1_000:.1f}K"
    
    # 3. Less than 1,000 (show exact number)
    else:
        return str(count)

# --- Testing the function ---
if __name__ == "__main__":
    test_counts = [450, 1500, 25300, 1200000, 5000000]
    
    print("Instagram Follower Formatting:")
    for count in test_counts:
        print(f"   {count:,} -> {format_follower_count(count)}")

