class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(nums):
            s = len(nums)
            l, r = 0, s-1
            while l <= r:
                c = (l+r)//2
                if nums[c] < target:
                    l = c+1
                elif nums[c] > target:
                    r = c-1
                else:
                    return True, c
            return False, r
        res, row = bsearch([row[0] for row in matrix])
        if res:
            return True
        if row < 0:
            return False
        return bsearch(matrix[row])[0]
