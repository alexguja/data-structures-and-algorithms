class MaxHeap:
    def __init__(self):
        self.data = []
        self.heap_size = 0

    def parent(self, i) -> int:
        return (i - 1) // 2

    def left(self, i) -> int:
        return 2 * i + 1

    def right(self, i) -> int:
        return 2 * i + 2

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < self.heap_size and self.data[left] > self.data[i]:
            largest = left

        if right <= self.heap_size and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            self.__swap(i, largest)
            i = largest

    def build_max_heap(self, array):
        """Builds a max heap from a list of elements."""

        self.data = array
        self.heap_size = len(array)
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def insert(self, key):
        """Inserts a new element into the heap."""

        self.heap_size += 1
        self.data.append(key)
        i = self.heap_size - 1
        self.__bubble_up(i)

    def increase_key(self, i, key):
        """Increases the value of element at index i to key."""

        if key < self.data[i]:
            raise ValueError("New key is smaller than current key")
        self.data[i] = key
        self.__bubble_up(i)

    def delete(self, i):
        """Deletes the element at index i."""
        self.increase_key(i, float("inf"))
        self.data[0] = self.data[self.heap_size - 1]
        self.data.pop()
        self.heap_size -= 1
        self.max_heapify(0)

    def max_element(self):
        """Returns the maximum element in the heap."""
        return self.data[0]

    def extract_max(self):
        """Extracts and returns the maximum element from the heap."""

        if self.heap_size < 1:
            raise IndexError("Heap underflow")

        max_element = self.data[0]
        self.data[0] = self.data[self.heap_size - 1]
        self.heap_size -= 1
        self.data.pop()
        self.max_heapify(0)

        return max_element

    def heapsort(self):
        """Sorts the array using heap sort."""
        self.build_max_heap(self.data)
        for i in range(len(self.data) - 1, 0, -1):
            self.__swap(0, i)
            self.heap_size -= 1
            self.max_heapify(0)

    def __swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bubble_up(self, i):
        while i > 0 and self.data[self.parent(i)] < self.data[i]:
            self.__swap(i, self.parent(i))
            i = self.parent(i)
    