# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mindist = 10**5
        self.last = 2*self.mindist
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.mindist = min(self.mindist, abs(node.val-self.last))
            self.last = node.val
            dfs(node.right)
        dfs(root)
        return self.mindist
