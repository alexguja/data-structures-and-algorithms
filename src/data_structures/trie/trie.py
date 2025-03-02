class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_entry = False  # Marks the end of an inserted word/entry.


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            # Add new character to the children hashmap if it doesn't exist
            if char not in current.children:
                current.children[char] = TrieNode()

            # Move to the next node
            current = current.children[char]

        # Mark the end of the entry
        current.is_entry = True

    def find(self, word: str) -> bool:
        current = self.root

        for char in word:
            # Detect missing node and return False
            if char not in current.children:
                return False

            # Move to the next node
            current = current.children[char]

        return current.is_entry  # Verify end of entry

    def starts_with(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            # Detect missing node and return False
            if char not in current.children:
                return False

            # Move to the next node
            current = current.children[char]

        return True
