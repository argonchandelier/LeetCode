# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(node):
            if not node:
                return False, False
            hasp, hasq = False, False
            if node is p:
                hasp = True
            if node is q:
                hasq = True
            haspl, hasql = dfs(node.left)
            if self.res:
                return True, True
            haspr, hasqr = dfs(node.right)
            if self.res:
                return True, True
            hasp, hasq = hasp or haspl or haspr, hasq or hasql or hasqr
            if hasp and hasq:
                self.res = node
            return hasp, hasq
        dfs(root)
        return self.res
        