class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx, reach = -1, len(nums)-1
        for i, num in enumerate(nums):
            s = i+num
            if s > mx:
                mx = s
                if mx >= reach:
                    return True
            if mx == i:
                return False