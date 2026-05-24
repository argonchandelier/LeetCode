"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        layer = [root, None]
        while len(layer) > 1:
            newlayer = []
            for i in range(len(layer)-1):
                node = layer[i]
                node.next = layer[i+1]
                if node.left:
                    newlayer.append(node.left)
                if node.right:
                    newlayer.append(node.right)
            newlayer.append(None)
            layer = newlayer
        
        return root
        