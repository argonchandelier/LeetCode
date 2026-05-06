class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 1
        end = nums[0]
        m = len(nums)-1
        if end >= m:
            return 1 if m > 0 else 0
        for i in range(2, len(nums)):
            newcur = end+1
            for j in range(cur, newcur):
                check = nums[j]+j
                if check > end:
                    end = check
                    if end >= m:
                        return i
            cur = newcur

