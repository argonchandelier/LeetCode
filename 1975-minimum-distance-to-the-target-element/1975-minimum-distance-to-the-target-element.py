class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        md = 1000
        for i, n in enumerate(nums):
            if n != target:
                continue
            md = min(md, abs(i - start))
        
        return md