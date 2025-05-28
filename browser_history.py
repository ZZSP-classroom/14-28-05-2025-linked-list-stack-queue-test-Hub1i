class BrowserHistory:
    def __init__(self):
        self.history = []

    # Push a new URL to the stack
    def push(self, url):
        self.history.append(url)

    # Pop the last visited URL
    def pop(self):
        if self.is_empty():
            return None
        return self.history.pop()

    # Peek at the last visited URL
    def peek(self):
        if self.is_empty():
            return None
        return self.history[-1]

    # Check if history is empty
    def is_empty(self):
        return len(self.history) == 0

# Test the Browser History Stack
if __name__ == "__main__":
    history = BrowserHistory()

    # Simulate browsing
    history.push("www.google.com")
    history.push("www.stackoverflow.com")
    history.push("www.github.com")

    print("Last visited:", history.peek())

    # Pop the last visited webpage
    print("Back to:", history.pop())
    print("Back to:", history.pop())
    print("Last visited after pop:", history.peek())
