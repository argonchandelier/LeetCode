class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ap = [0]*k
        self.res = []
        def bt(mn, i):
            if i == k:
                self.res.append(self.ap[:])
                return
            for num in range(mn, n-k+i+2):
                self.ap[i] = num
                bt(num+1, i+1)
        bt(1, 0)
        return self.res