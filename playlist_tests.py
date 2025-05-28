import unittest
from playlist_manager import Playlist

class TestPlaylistManager(unittest.TestCase):

    def test_add_and_remove_song(self):
        playlist = Playlist()
        playlist.add_song("Song 1", "Artist A")
        playlist.add_song("Song 2", "Artist B")
        playlist.remove_song("Song 1")
        self.assertEqual(playlist.get_next_song(), "Song 2")

if __name__ == '__main__':
    unittest.main()
