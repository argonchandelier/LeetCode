# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.last = None
        def dfs(node):
            nxt = None
            if node.left:
                dfs(node.left)
                nxt = node.left
            if node.right:
                if not nxt:
                    nxt = node.right
                else:
                    self.last.right = node.right
                dfs(node.right)
            node.left = None
            node.right = nxt
            if not nxt:
                self.last = node
        dfs(root)