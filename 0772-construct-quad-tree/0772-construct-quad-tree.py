"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dac(r, c, size):
            if size == 1:
                return Node(grid[r][c], 1)
            ns = size // 2
            r2, c2 = r+ns, c+ns
            children = (dac(r, c, ns), dac(r, c2, ns), dac(r2, c, ns), dac(r2, c2, ns))
            if sum(node.isLeaf for node in children) == 4 and sum(node.val for node in children) in {0, 4}:
                return children[0]
            return Node(0, 0, *children)
        return dac(0, 0, len(grid))


        