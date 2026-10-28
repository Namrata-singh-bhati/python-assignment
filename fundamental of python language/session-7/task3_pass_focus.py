# ==============================================================================
# Task 3: Handle 'Focus' Playlist Using pass
# File: session-6/task3_pass_focus.py
# Purpose: Loop through playlists, use 'pass' when the playlist is 'Focus',
#          and print all other playlists.
# ==============================================================================

# What does 'pass' do?
# 'pass' is a placeholder that does absolutely nothing.
# Python requires a statement inside an 'if' block, so we use 'pass'
# when we don't want to execute any code.

playlists = ['Chill Vibes', 'Workout', 'Focus', 'Party']

print("Playlists (using pass for 'Focus'):")

for playlist in playlists:
    if playlist == 'Focus':
        # Do nothing when playlist is 'Focus'
        pass
    else:
        # Print all other playlists
        print(playlist)

