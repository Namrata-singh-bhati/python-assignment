# ==============================================================================
# Task 3: Display Friends and Followers Function
# File: session-10/task3_display_friends.py
# Purpose: Write display_friends(friends) to print: 'username: 2.3K followers'.
# ==============================================================================

def display_friends(friends):
    # Loop through the dictionary using items() to get both username and followers
    for username, followers in friends.items():
        print(f"{username}: {followers} followers")

# --- Testing the function ---
if __name__ == "__main__":
    instagram_friends = {
        'priya_travels': '2.3K',
        'rahul_music': '15.8K',
        'rohit_fitness': '850',
        'sneha_art': '4.1K'
    }
    
    print("Instagram Friends List:")
    display_friends(instagram_friends)

