class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_entry = False  # Marks the end of an inserted word/entry.


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pass

    def find(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass
