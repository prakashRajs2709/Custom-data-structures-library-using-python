from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    
    def __repr__(self):
        nodes = []
        queue = deque([self.root])
        if self.root is None:
            return f"Binary Tree is empty Nothing to display"
        while queue:
            cur_node = queue.popleft()
            if cur_node is not None:
                nodes.append(str(cur_node.data))
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            
            else:
                nodes.append("None")
        
        while nodes and nodes[-1] == 'None':
            nodes.pop()
        return f"[{ '|'.join(nodes)}]"
    
    

bt = BinaryTree(1)
print(bt)

