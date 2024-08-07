class TableEntry:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.count = 0
        self.resize_lower_bound = 0.25
        self.resize_upper_bound = 0.75

    def insert(self, key, value):

        # Check if the key already exists
        existing_entry = self.find(key)
        if existing_entry:
            # If the entry already exists, overwrite the value
            existing_entry.value = value
        else:
            # Prepend the new entry to the linked list
            index = self.__simple_hash(key)
            self.table[index] = TableEntry(key, value, self.table[index])
            self.count += 1

        # Grow the table if necessary
        if self.count / self.size >= self.resize_upper_bound:
            self.__resize(2 * self.size)

    
    def find(self, key) -> TableEntry:
        """Finds a value in the hash table.

        Args:
            key str: The key to search for.

        Returns:
            TableEntry: The entry with the given key, or None if the key is not found.
        """
        index = self.__simple_hash(key)
        entry = self.table[index]
        while entry:
            if entry.key == key:
                return entry.value
            entry = entry.next
        return None
    

    def delete(self, key):
        index = self.__simple_hash(key)
        entry = self.table[index]
        prev_entry = None

        while entry:
            # Match found by key
            if entry.key == key:
                # Remove a node from the linked list that is not the head
                if prev_entry:
                    prev_entry.next = entry.next
                else:
                    self.table[index] = entry.next
                self.count -= 1

                # Shrink the table if necessary
                if self.count / self.size <= self.resize_lower_bound:
                    self.__resize(self.size // 2)
                
                return entry.value
            
            prev_entry = entry
            entry = entry.next
        return None
    

    def __simple_hash(self, key):
        return sum(ord(char) for char in key) % self.size
    
    def __resize(self, new_size):
        new_table = HashTable(new_size)
        for entry in self.table:
            while entry:
                new_table.insert(entry.key, entry.value)
                entry = entry.next
        self.size = new_table.size
        self.table = new_table.table
    




