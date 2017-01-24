class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root == None:
            return False
        else:
            return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if self.root == None:
            return ""
        else:
            trav_list = []
            return self.preorder_print(self.root, trav_list)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start == None: 
            return False
        elif start.value == find_val:
            return True
        else:
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start != None:
            traversal.append(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root == None:
            self.root = Node(new_val)
        else:
            current = self.root
            while current.value <= new_val:
                if current.right == None:
                    current.right = Node(new_val)
                    break
                else:
                    current = current.right
                    
            while current.value > new_val:
                if current.left == None:
                    current.left = Node(new_val)
                    break
                else:
                    current = current.left
    
    def search(self, find_val):
        return False


tree = BST(4)

tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.search(4)
print tree.search(6)

# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# # Test search
# # Should be True
# print tree.search(4)
# print tree.search(3)
# # Should be False
# print tree.search(6)

# # Test print_tree
# # Should be 1-2-4-5-3
# print tree.print_tree()
