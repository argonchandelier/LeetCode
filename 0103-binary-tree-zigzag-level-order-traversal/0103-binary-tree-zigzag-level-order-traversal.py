# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        layer = [root]
        rev = False
        while layer:
            res.append([node.val for node in (layer[::-1] if rev else layer)])
            rev = not rev
            newlayer = []
            for node in layer:
                if node.left:
                    newlayer.append(node.left)
                if node.right:
                    newlayer.append(node.right)
            layer = newlayer
        return res