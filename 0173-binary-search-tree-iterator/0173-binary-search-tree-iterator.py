# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.path = [root]
        while self.path[-1].left:
            self.path.append(self.path[-1].left)
            self.path[-2].left = None

    def next(self) -> int:
        val = self.path[-1].val
        if self.path[-1].right:
            self.path[-1] = self.path[-1].right
            while self.path[-1].left:
                self.path.append(self.path[-1].left)
                self.path[-2].left = None
        else:
            self.path.pop()
        return val

    def hasNext(self) -> bool:
        return len(self.path) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()