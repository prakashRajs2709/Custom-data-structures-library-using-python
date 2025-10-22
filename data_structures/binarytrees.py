class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add_nodes(self, val, parent_val, direction):
        new_node = Node(val)
        direction_lower = None
        if direction is not None:
            direction_lower = direction.lower()
        if self.root is None:
            if parent_val is None:
                self.root = new_node
                return True
            else:
                print(f"Error: Root must be added first. Cannot find parent {parent_val}.")
                return False

        if self.root.val == parent_val:
            if direction_lower == 'left':
                if self.root.left is None:
                    self.root.left = new_node
                    return True
                else:
                    print(f"Error: Left child of {parent_val} is already occupied.")
                    return False
            elif direction_lower == 'right':
                if self.root.right is None:
                    self.root.right = new_node
                    return True
                else:
                    print(f"Error: Right child of {parent_val} is already occupied.")
                    return False
            else:
                print("Error: Direction must be 'left' or 'right'.")
                return False

        return self._add_recursive(self.root, new_node, parent_val, direction_lower)

    def _add_recursive(self, current_node, new_node, target_val, direction):
        if current_node is None:
            return False
        if current_node.val == target_val:
            if direction == 'left':
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                else:
                    print(f"Error: Left child of {target_val} is already occupied.")
                    return False
            elif direction == 'right':
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                else:
                    print(f"Error: Right child of {target_val} is already occupied.")
                    return False
        if self._add_recursive(current_node.left, new_node, target_val, direction):
            return True
        
        return self._add_recursive(current_node.right, new_node, target_val, direction)
        
    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

    def levelorder(self,root):
        if self.root is None:
            print("Tree is empty")
            return
        
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

#    1
#   / \
#  2   3
# /     \
# 4      5

# tree = BinaryTree()
# tree.add_nodes(1, None, None)
# tree.add_nodes(2, 1, 'left')
# tree.add_nodes(3, 1, 'right')
# tree.add_nodes(4, 2, 'left')
# tree.add_nodes(5, 3, 'right')

# print("In-Order Traversal:")
# tree.inorder(tree.root)
# print("\nPre-Order Traversal:")
# tree.preorder(tree.root)
# print("\nPost-Order Traversal:")
# tree.postorder(tree.root)
# print("\nLevel Order Traversal")
# tree.levelorder(tree.root)