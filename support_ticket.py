class Ticket:
    def __init__(self, ticket_id, issue_description):
        self.ticket_id = ticket_id
        self.issue_description = issue_description

    def __repr__(self):
        return f"Ticket({self.ticket_id}, {self.issue_description})"

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Test the Ticket System
if __name__ == "__main__":
    # Create a queue for incoming tickets and a stack for processing tickets
    incoming_queue = Queue()
    processing_stack = Stack()

    # Create ticket objects
    ticket1 = Ticket(1, "Issue with login")
    ticket2 = Ticket(2, "Payment failed")
    ticket3 = Ticket(3, "Page not loading")

    # Enqueue tickets
    incoming_queue.enqueue(ticket1)
    incoming_queue.enqueue(ticket2)
    incoming_queue.enqueue(ticket3)

    # Process the first ticket
    processing_stack.push(incoming_queue.dequeue())
    processing_stack.push(incoming_queue.dequeue())

    # Print the ticket being processed
    print("Processing ticket:", processing_stack.pop())
    print("Processing ticket:", processing_stack.pop())
