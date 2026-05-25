# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -1000
        def dfs(node):
            if not node:
                return 0
            lpath = dfs(node.left)
            rpath = dfs(node.right)
            mx = node.val + max(0, lpath) + max(0, rpath)
            self.max = max(self.max, mx)
            return node.val + max(lpath, rpath, 0)
        dfs(root)
        return self.max