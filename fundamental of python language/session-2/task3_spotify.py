# ==============================================================================
# Task 3: Spotify Playlist Memory Addresses
# File: session-2/task3_spotify.py
# Purpose: Create playlist variables and print their memory addresses using id().
# ==============================================================================

# In Python, every variable is stored at a specific location in computer memory (RAM).
# The built-in id() function gives us that unique memory address (like a house address).

# Step 1: Create the three variables
playlist_title = "Morning Motivation"
number_of_songs = 35
is_public = True

# Step 2: Print each variable and its unique memory address using id()
print("Variable: playlist_title")
print("Value         :", playlist_title)
print("Memory Address:", id(playlist_title))
print()

print("Variable: number_of_songs")
print("Value         :", number_of_songs)
print("Memory Address:", id(number_of_songs))
print()

print("Variable: is_public")
print("Value         :", is_public)
print("Memory Address:", id(is_public))

