from numpy import array
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        inds = defaultdict(list)
        nearest = {}
        n = len(nums)
        rep = [0]*n
        for i, num in enumerate(nums):
            rep[i] = len(inds[num])
            inds[num].append(i)

        for i, indl in inds.items():
            m = len(indl)
            if m < 2:
                continue
            nearesti = [0]*m
            for j, ind in enumerate(indl):
                prevd = abs(ind - indl[j-1])
                nextd = abs(ind - indl[(j+1) % m])
                nearesti[j] = min(prevd, nextd, n-prevd, n-nextd)
            nearest[i] = nearesti
        
        ans = [-1]*len(queries)
        for i, q in enumerate(queries):
            num = nums[q]
            if num not in nearest:
                continue
            ans[i] = nearest[num][rep[q]]

        return ans