from data_structures.treesusinginkedlists import BinaryTree

tree = BinaryTree()
tree.add_nodes(1, None, None)
tree.add_nodes(2, 1, 'left')
tree.add_nodes(3, 1, 'right')
tree.add_nodes(4, 2, 'left')
tree.add_nodes(5, 3, 'right')

print("In-Order Traversal:")
tree.inorder(tree.root)
print("\nPre-Order Traversal:")
tree.preorder(tree.root)
print("\nPost-Order Traversal:")
tree.postorder(tree.root)
print("\nLevel Order Traversal")
tree.levelorder(tree.root)