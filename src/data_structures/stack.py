class Stack:
    def __init__(self, stack_size=10):
        self.stack_size = stack_size
        self.stack = [0] * self.stack_size
        self.top = -1

    def push(self, x):
        if self.top == self.stack_size - 1:
            raise ValueError("Stack overflow")
        self.top += 1
        self.stack[self.top] = x
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        self.top -= 1
        return self.stack[self.top + 1]
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1