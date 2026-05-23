# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        layer = [root]
        nlayers = 0
        while layer:
            newlayer = []
            for node in layer:
                if node.left:
                    newlayer.append(node.left)
                if node.right:
                    newlayer.append(node.right)
            nlayers += 1
            layer = newlayer
        
        return nlayers
            
            
        