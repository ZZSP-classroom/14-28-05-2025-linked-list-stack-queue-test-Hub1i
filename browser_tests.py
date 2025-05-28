import unittest
from browser_history import BrowserHistory

class TestBrowserHistory(unittest.TestCase):

    def test_push_pop(self):
        history = BrowserHistory()
        history.push("www.google.com")
        self.assertEqual(history.pop(), "www.google.com")

    def test_peek(self):
        history = BrowserHistory()
        history.push("www.google.com")
        self.assertEqual(history.peek(), "www.google.com")

    def test_empty_history(self):
        history = BrowserHistory()
        self.assertIsNone(history.pop())
        self.assertIsNone(history.peek())

if __name__ == '__main__':
    unittest.main()
