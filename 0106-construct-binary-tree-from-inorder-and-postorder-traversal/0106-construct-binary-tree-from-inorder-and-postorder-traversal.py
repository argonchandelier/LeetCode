# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        iomap = {val: i for i, val in enumerate(inorder)}
        self.poi = len(postorder)-1
        def traverse(s, e):
            if e < s:
                return None
            val = postorder[self.poi]
            self.poi -= 1
            node = TreeNode(val)
            ioindex = iomap[val]
            node.right = traverse(ioindex+1, e)
            node.left = traverse(s, ioindex-1)
            return node
        return traverse(0, len(inorder)-1)