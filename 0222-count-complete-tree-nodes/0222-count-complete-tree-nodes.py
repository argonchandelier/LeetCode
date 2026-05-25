# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def countleft(node):
            c = 1
            while node.left:
                c += 1
                node = node.left
            return c
        def countright(node):
            c = 1
            while node.right:
                c += 1
                node = node.right
            return c
        cl, cr = countleft(root), countright(root)
        res = 2**cr - 1
        if cl == cr:
            return res
        head = root
        for i in range(1, cr):
            cm = i + countright(head.left)
            if cm == cl:
                head = head.right
                res += 2**(cr-i)
            else:
                head = head.left
        res += int(head.left is not None)

        return res
