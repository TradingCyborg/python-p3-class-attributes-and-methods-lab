class Song:
    # Class attribute to keep track of the number of songs
    count = 0

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

        # Call the class method to increment the count
        Song.add_song_to_count()

    @classmethod
    def add_song_to_count(cls):
        # Increment the class attribute count when a new song is created
        cls.count += 1

# Example usage:
song1 = Song("Song 1", "Artist 1")
song2 = Song("Song 2", "Artist 2")

# Accessing the class attribute count
print(f"Total number of songs: {Song.count}")
