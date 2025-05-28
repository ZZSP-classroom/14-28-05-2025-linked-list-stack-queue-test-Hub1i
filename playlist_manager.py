class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = SongNode(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song

    def remove_song(self, title):
        current = self.head
        if current and current.title == title:
            self.head = current.next
            return
        prev = None
        while current:
            if current.title == title:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def get_next_song(self):
        return self.head.title if self.head else None

# Test the Playlist system
if __name__ == "__main__":
    playlist = Playlist()

    playlist.add_song("Song 1", "Artist A")
    playlist.add_song("Song 2", "Artist B")
    playlist.add_song("Song 3", "Artist C")

    print("Next song:", playlist.get_next_song())

    playlist.remove_song("Song 2")

    print("Next song after removal:", playlist.get_next_song())
