class ListNode:
    def __init__(self, key, data, next=None, prev=None):
        self.key = key
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    """A singly linked list implementation"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, key, data):
        """Inserts a new node at the head of the list."""

        node = ListNode(key, data)
        node.next = self.head
        self.head = node

    def append(self, key, data):
        """Inserts a new node at the tail of the list."""

        node = ListNode(key, data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def delete_head(self) -> ListNode:
        """Deletes the head node of the list.

        Returns:
            ListNode: The node that was deleted or None if the list is empty
        """
        if self.is_empty():
            return None

        node = self.head  # node to delete
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return node

    def delete_tail(self) -> ListNode:
        """Deletes the tail node from the list.
        Returns:
            ListNode: The node that was deleted or None if the list is empty
        """
        if self.is_empty():
            return None

        if self.head == self.tail:
            return self.delete_head()

        prev = self.head
        while prev.next != self.tail:
            prev = prev.next

        node = self.tail
        self.tail = prev
        self.tail.next = None
        self.size -= 1
        return node

    def delete(self, key) -> ListNode:
        """Deletes a node from the list based on the given key.
        Args:
            key: The key of the node to delete

        Returns:
            ListNode: The node that was deleted or None if the key is not found
        """

        # Empty list edge case
        if self.__is_empty():
            return None

        # If the key is the head
        if self.head.key == key:
            return self.delete_head()

        # Traverse to find the previous node to the node to delete
        prev = self.head
        node = self.head.next  # node to delete

        while node and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        # Skip over the node to delete
        prev.next = node.next

        # If the node to delete is the tail, update the tail pointer
        if node == self.tail:
            return self.delete_tail()

        self.size -= 1
        return node

    def find(self, key) -> ListNode:
        """Returns the node containing the search key.

        Args:
            key: The key to search for

        Returns:
            ListNode: The node containing the search key or None if the data is not found
        """
        node = self.head  # current node

        # Time Complexity: O(n) - need to traverse the entire list in the worst case
        while node and node.key != key:
            node = node.next
        return node

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise."""

        return self.head is None
