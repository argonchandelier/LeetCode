# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, summ):
            if not node:
                return False
            summ += node.val
            if not node.left and not node.right:
                return targetSum == summ
            return dfs(node.left, summ) or dfs(node.right, summ)
        return dfs(root, 0)