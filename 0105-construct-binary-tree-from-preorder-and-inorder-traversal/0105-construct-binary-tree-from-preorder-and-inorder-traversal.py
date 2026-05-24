# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iomap = {}
        for i, val in enumerate(inorder):
            iomap[val] = i

        self.pi = 0
        def traverse(s, e):
            if e < s:
                return None
            val = preorder[self.pi]
            self.pi += 1
            node = TreeNode(val)
            ioindex = iomap[val]
            node.left = traverse(s, ioindex-1)
            node.right = traverse(ioindex+1, e)
            return node
        
        return traverse(0, len(preorder)-1)