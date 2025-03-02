class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0