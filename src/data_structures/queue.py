from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def enqueue(self, value):
        self.queue.insert_last(value)


    def dequeue(self):
        if self.queue.is_empty():
            return None
        else:
            dequeued_value = self.queue.head.data
            self.queue.delete_first()
            return dequeued_value
