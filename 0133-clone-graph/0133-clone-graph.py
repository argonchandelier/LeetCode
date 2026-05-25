"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = Node(node.val)
        seen = {node: root}
        check = [node]
        while check:
            node = check.pop()
            copynode = seen[node]
            for nb in node.neighbors:
                if nb in seen:
                    copynode.neighbors.append(seen[nb])
                    continue
                nn = Node(nb.val)
                seen[nb] = nn
                copynode.neighbors.append(nn)
                check.append(nb)
        
        return root

