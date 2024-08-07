class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = TreeNode(key, value)

        node = None        # current node
        parent = self.root # parent of the current node

        while parent is not None:
            node = parent
            if new_node.key < parent.key:
                parent = parent.left
            else:
                parent = parent.right
        
        new_node.parent = node

        # Edge case for an empty tree
        if node is None:
            self.root = new_node
        elif new_node.key < node.key:
            node.left = new_node
        else:
            node.right = new_node


    def delete(self, key):
        pass 

    def in_order_traversal(self):
        """Performs an in-order tree walk."""

        if self.root:
            self.in_order_traversal(self.root.left)
            print(self.root.key)
            self.in_order_traversal(self.root.right)
        
    
    def find(self, key):
        """Finds a node with the given key in the BST"""

        if self.root is None or self.root.key == key:
            return self.root
        if key < self.root.key:
            return self.find(self.root.left, key)
        else:
            return self.find(self.root.right, key)
        
    
    def find_iterative(self, key):
        """Finds a node with the given key in the BST iteratively."""

        node = self.root

        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node


    def minimum(self, node):
        """Finds the minimum key in the BST."""

        while node.left is not None:
            node = node.left

        return node
    
    def maximum(self, node):
        """Finds the maximum key in the BST."""

        while node.right is not None:
            node = node.right

        return node
    
    def successor(self, node):
        """Finds the successor of a given node."""

        if node.right is not None:
            return self.minimum(node.right)
        
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        
        return parent