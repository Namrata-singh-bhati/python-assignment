# ==============================================================================
# Task 2: Add and Update Entries in Dictionary
# File: session-10/task2_modify_playlist.py
# Purpose: Add a new song to my_playlist, then update the duration of an existing song.
# ==============================================================================

my_playlist = {
    'Blinding Lights': 3.20,
    'Shape of You': 3.53,
    'Levitating': 3.23
}

print("Original Playlist:")
print(my_playlist)

# 1. Add a new song and its duration
# Assigning to a new key automatically adds it to the dictionary
my_playlist['Stay'] = 2.21
print("\nAfter adding new song 'Stay':")
print(my_playlist)

# 2. Update the duration of an existing song
# Assigning to an existing key updates its value
my_playlist['Blinding Lights'] = 3.35
print("\nAfter updating duration for 'Blinding Lights':")
print(my_playlist)

