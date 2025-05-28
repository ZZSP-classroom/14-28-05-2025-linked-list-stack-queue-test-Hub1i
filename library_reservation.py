# Create a Queue class to handle reservations
class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title

    def __repr__(self):
        return f"Reservation({self.user_name}, {self.book_title})"

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue reservation
    def enqueue(self, reservation):
        self.queue.append(reservation)

    # Dequeue reservation (removes and returns the first item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    # Peek at the first reservation
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Test the Queue class
if __name__ == "__main__":
    # Create a Queue for library reservations
    library_queue = Queue()

    # Create reservation objects
    reservation1 = Reservation("example", "example")
    reservation2 = Reservation("example", "1982")
    reservation3 = Reservation("example", "example")

    # Enqueue reservations
    library_queue.enqueue(reservation1)
    library_queue.enqueue(reservation2)
    library_queue.enqueue(reservation3)

    # Print the next reservation
    print("Next reservation:", library_queue.peek())

    # Dequeue reservations and print
    print("Dequeue reservation:", library_queue.dequeue())
    print("Dequeue reservation:", library_queue.dequeue())

    # Peek again after dequeue
    print("Next reservation after some dequeues:", library_queue.peek())
