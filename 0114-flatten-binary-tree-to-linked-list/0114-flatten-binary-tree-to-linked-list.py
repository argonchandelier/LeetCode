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
        self.last = TreeNode()
        def dfs(node):
            if node is None:
                return
            self.last.left = node
            self.last = node
            dfs(node.left)
            dfs(node.right)
            node.right = None

        dfs(root)
        head = root
        while head:
            head.left, head.right, head = None, head.left, head.left