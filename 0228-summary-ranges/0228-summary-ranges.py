class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        a = nums[0]
        b = a
        res = []
        cut = len(nums)-1
        for i, num in enumerate(nums[1:], start=1):
            if b+1 == num:
                b += 1
                continue
            add = str(a)+"->"+str(b) if a != b else str(a)
            res.append(add)
            a = b = num
        add = str(a)+"->"+str(b) if a != b else str(a)
        res.append(add)
        
        return res
        