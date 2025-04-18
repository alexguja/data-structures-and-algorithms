INFNITY = float("inf")

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def parent(self, i) -> int:
        return (i - 1) // 2

    def left(self, i) -> int:
        return 2 * i + 1

    def right(self, i) -> int:
        return 2 * i + 2

    def max_heapify(self, i):
        """Maintains the max heap property.

        Args:
            i (int): Index of the element to heapify.
        """
        # Time complexity: O(lg n)
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < self.heap_size and self.heap[left] > self.heap[i]:
            largest = left

        if right < self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.__swap(i, largest)
            i = largest

    def max_heapify_iterative(self, i):
        # Time complexity: O(lg n)
        while i < self.heap_size:
            left = self.left(i)
            right = self.right(i)
            largest = i

            if left < self.heap_size and self.heap[left] > self.heap[i]:
                largest = left

            if right <= self.heap_size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.__swap(i, largest)
                i = largest

    def build_max_heap(self, array):
        """Builds a max heap from a list of elements."""

        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def insert(self, key):
        """Inserts a new element into the heap."""

        self.heap_size += 1
        self.heap.append(key)
        self.__bubble_up(self.heap_size - 1)

    def increase_key(self, i, key):
        """Increases the value of element at index i to key."""

        if key < self.heap[i]:
            raise ValueError("New key is smaller than current key")
        self.heap[i] = key
        self.__bubble_up(i) # Time Complexity: O(lg n)

    def delete(self, i):
        """Deletes the element at index i."""
        
        self.increase_key(i, INFNITY)
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap.pop() # Optional step
        self.heap_size -= 1
        self.max_heapify(0) # Time Complexity: O(lg n)

    def max_element(self):
        """Returns the maximum element in the heap."""
        return self.heap[0] # Time Complexity: O(1)

    def extract_max(self):
        """Extracts and returns the maximum element from the heap."""

        # Time complexity: O(lg n)
        if self.heap_size < 1:
            raise IndexError("Heap underflow")

        max_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.heap.pop()
        self.max_heapify(0) # O(lg n)

        return max_element

    def heapsort(self):
        """Sorts a heap in place.
        The heapsort algorithm works by first building a max heap from the input array.
        The max element is located at the root of the heap. It can be extracted to the end of the array.
        The heap size is reduced by one and the heap is max heapified to restore the max heap property.
        This process is repeated until the heap is empty.
        """

        # Time complexity: O(n lg n)
        self.build_max_heap(self.heap) # O(n)
        for i in range(len(self.heap) - 1, 0, -1):
            self.__swap(0, i)
            self.heap_size -= 1
            self.max_heapify(0) # O(lg n)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __bubble_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.__swap(i, self.parent(i))
            i = self.parent(i)
    