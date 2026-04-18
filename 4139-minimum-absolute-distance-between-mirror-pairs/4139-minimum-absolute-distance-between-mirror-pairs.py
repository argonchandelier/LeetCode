from functools import lru_cache

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}
        dist = float('inf')

        @lru_cache(None)
        def reverse(num):
            return int(str(num)[::-1])

        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            rev = reverse(num)
            if rev in mp:
                dist = min(dist, mp[rev]-i)
            mp[num] = i
        
        return dist if dist < float('inf') else -1