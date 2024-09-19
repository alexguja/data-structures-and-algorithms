class DynamicArray:
    def __init__(self):
        self.n = 0  
        self.capacity = 1  
        self.array = self.__make_array(self.capacity)

    def append(self, item):
        if self.n == self.capacity:
            self.__resize(2 * self.capacity) 
        self.array[self.n] = item
        self.n += 1

    def insert(self, index, item):
        if not 0 <= index <= self._n:
            raise IndexError("index out of bounds")
        
        if self.n == self._capacity:
            self.__resize(2 * self.capacity)  

        # Shift elements to the right to make space for the new element
        for i in range(self.n, index, -1):
            self.array[i] = self.array[i - 1]
        
        # Insert the new element
        self.array[index] = item
        self.n += 1

    def __resize(self, new_capacity):
        new_array = self.__make_array(new_capacity)  
        for i in range(self._n):
            new_array[i] = self.array[i]  # Copy old elements
        self.array = new_array  # Replace old array with new array
        self.capacity = new_capacity

    def __make_array(self, capacity):
        return [None] * capacity  # Create a new array with given capacity
    
    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('index out of bounds')
        return self._array[index]

# # Example usage

# dynamic_array = DynamicArray()
# dynamic_array.append(1)
# dynamic_array.append(2)
# dynamic_array.append(4)

# print("Before Insertion:", [dynamic_array[i] for i in range(len(dynamic_array))])

# dynamic_array.insert(2, 3)

# print("After Insertion:", [dynamic_array[i] for i in range(len(dynamic_array))])
