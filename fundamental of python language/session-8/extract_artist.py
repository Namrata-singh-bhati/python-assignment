# ==============================================================================
# Task 2: Extract Artist Name from Spotify Song Title
# File: session-7/extract_artist.py
# Purpose: Write a function extract_artist(song_title) that returns just the artist's
#          name using index() and string slicing.
# ==============================================================================

def extract_artist(song_title):
    # Hint: Use index() to find the position of the dash '-'
    dash_index = song_title.index('-')
    
    # String slicing: slice from after the dash to the end of the string
    # .strip() removes any extra spaces around the artist's name
    artist = song_title[dash_index + 1:].strip()
    
    return artist

# --- Testing the function ---
if __name__ == "__main__":
    sample_song1 = "Blinding Lights - The Weeknd"
    sample_song2 = "Shape of You - Ed Sheeran"
    
    print("Song 1 Artist:", extract_artist(sample_song1))
    print("Song 2 Artist:", extract_artist(sample_song2))

