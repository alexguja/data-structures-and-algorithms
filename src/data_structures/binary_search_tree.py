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

        while parent:
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
        node = self.root
        parent = None

        # Find the node to delete and its parent
        while node and node.key != key:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if node is None:
            return  # Node to be deleted not found

        # Case 1: Node to be deleted has no children
        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
            elif node == parent.left:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node to be deleted has one child
        elif node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if node == self.root:
                self.root = child
            elif node == parent.left:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node to be deleted has two children
        else:
            successor = self.minimum(node.right)
            node.key, node.value = successor.key, successor.value
            self.__delete_successor(node.right, successor.key)


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

        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node


    def minimum(self, node):
        """Finds the minimum key in the BST."""

        while node.left:
            node = node.left

        return node
    
    def maximum(self, node):
        """Finds the maximum key in the BST."""

        while node.right:
            node = node.right

        return node
    
    def successor(self, node):
        """Finds the successor of a given node."""

        if node.right:
            return self.minimum(node.right)
        
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        
        return parent
    
    def __delete_successor(self, node, key):
        parent = None
        while node and node.key != key:
            parent = node
            node = node.left

        if parent.left == node:
            parent.left = node.right
        else:
            parent.right = node.right