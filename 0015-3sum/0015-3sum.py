from collections import Counter, defaultdict
from bisect import bisect_right

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        n = len(nums)
        res = []
        keys = sorted(list(counts.keys()))
        m = len(keys)
        for i, n1 in enumerate(keys):
            counts[n1] -= 1
            for j in range(i if counts[n1] > 0 else i+1, m):
                n2 = keys[j]
                goal = -(n1+n2)
                if goal < n2:
                    break
                if counts[goal] > (0 if goal != n2 else 1):
                    res.append([n1, n2, goal])
            counts[n1] = 0
        
        return res
    '''
    Contains duplicate triplets
        #nums.sort()
        #counts = Counter(nums)
        n = len(nums)
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        #p1, p2 = 0, len(nums)-1
        res = []
        for i, n1 in enumerate(nums[:-2]):
            for j in range(i+1, n-1):
                n2 = nums[j]
                goal = -(n1+n2)
                if goal not in d:
                    continue
                arr = d[goal]
                print(i, j, arr)
                for k in range(bisect_right(arr, j), len(arr)):
                    k2 = arr[k]
                    res.append([n1, n2, nums[k2]])
        
        return res
    '''
                
