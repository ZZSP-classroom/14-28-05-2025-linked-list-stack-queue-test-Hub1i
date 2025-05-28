import unittest
from library_reservation import Queue, Reservation

class TestLibraryQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        q = Queue()
        r1 = Reservation("exxx", "exxx")
        q.enqueue(r1)
        self.assertEqual(q.dequeue().user_name, "exxx")

    def test_peek(self):
        q = Queue()
        r1 = Reservation("exxx", "exxx")
        q.enqueue(r1)
        self.assertEqual(q.peek().user_name, "exxx")

    def test_empty_queue(self):
        q = Queue()
        self.assertIsNone(q.dequeue())
        self.assertIsNone(q.peek())

if __name__ == '__main__':
    unittest.main()
