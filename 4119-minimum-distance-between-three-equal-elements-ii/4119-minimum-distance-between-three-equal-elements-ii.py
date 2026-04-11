class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexes = {}
        minDist = float('inf')
        for i, n in enumerate(nums):
            if n not in indexes:
                indexes[n] = [i]
                continue
            if len(indexes[n]) < 3:
                indexes[n].append(i)
                if len(indexes[n]) < 3:
                    continue
            else:
                indexes[n][0], indexes[n][1], indexes[n][2] = indexes[n][1], indexes[n][2], i

            minDist = min(minDist, 2*(indexes[n][2] - indexes[n][0]))

        return minDist if minDist < float('inf') else -1
        
        
        
