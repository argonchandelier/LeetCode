class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        s = set(nums)
        res = 0
        for i, n in enumerate(s):
            if n in seen:
                continue
            seen.add(n)
            nl, nr = n-1, n+1
            while nl in s:
                seen.add(nl)
                nl -= 1
            while nr in s:
                seen.add(nr)
                nr += 1
            res = max(res, nr-nl-1)
        
        return res

