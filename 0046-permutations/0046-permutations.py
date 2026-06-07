class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.left = set(nums)
        self.perm = nums[:]
        self.res = []
        n = len(nums)
        def bs(i):
            if i == n:
                self.res.append(self.perm[:])
                return
            for left in list(self.left):
                self.left.remove(left)
                self.perm[i] = left
                bs(i+1)
                self.left.add(left)
        bs(0)
        return self.res
