# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        c = len(nums) // 2
        return TreeNode(nums[c], self.sortedArrayToBST(nums[:c]), 
                                 self.sortedArrayToBST(nums[c+1:]))

            