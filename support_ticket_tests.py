import unittest
from support_ticket import Queue, Stack, Ticket

class TestSupportTicketSystem(unittest.TestCase):

    def test_ticket_enqueue_dequeue(self):
        q = Queue()
        ticket1 = Ticket(1, "Issue with login")
        q.enqueue(ticket1)
        self.assertEqual(q.dequeue().ticket_id, 1)

    def test_ticket_processing_stack(self):
        stack = Stack()
        ticket1 = Ticket(1, "Issue with login")
        stack.push(ticket1)
        self.assertEqual(stack.pop().ticket_id, 1)

if __name__ == '__main__':
    unittest.main()
