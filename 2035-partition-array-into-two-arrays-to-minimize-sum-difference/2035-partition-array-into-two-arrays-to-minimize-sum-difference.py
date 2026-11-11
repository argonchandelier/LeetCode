class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        l = len(nums)
        l2 = l // 2
        ns1, ns2 = nums[:l2], nums[l2:]
        #sums1, sums2 = [set() for _ in range(l2)], [set() for _ in range(l2)]
        #sums1[0], sums2[0] = set(ns1), set(ns2)
        self.target = sum(nums) / 2

        def get_sums(array):
            res = [set() for _ in range(l2+1)]
            res[0].add(0)
            for x in array:
                for k in range(l2, 0, -1):
                    for n in res[k-1]:
                        res[k].add(n + x)
            
            return [sorted(list(x)) for x in res[1:]]

        sums1, sums2 = get_sums(ns1), get_sums(ns2)
        self.best = abs(sums1[-1][0] - self.target) #float('inf')
        #print(sums1, sums2, self.best, f"{self.target=}")

        def smallest_diff(a1, a2):
            p2t = len(a2)-1
            for v in a1:
                t = self.target - v
                p1, p2 = 0, p2t
                while p1 < p2-1:
                    pm = (p1 + p2) // 2
                    nm = a2[pm]
                    if nm < t:
                        p1 = pm
                    elif nm > t:
                        p2 = pm
                    else:
                        self.best = 0
                        return
                n1, n2 = a2[p1], a2[p2]
                d1, d2 = abs(t-n1), abs(t-n2)
                #print(a1, a2, t, n1, n2, d1, d2)
                if d1 <= d2:
                    self.best = min(d1, self.best)
                    p2t = p1
                else:
                    self.best = min(d2, self.best)
                    p2t = p2

        for k in range(l2-1):
            ar1, ar2 = sums1[k], sums2[-k-2]
            smallest_diff(ar1, ar2)
            if self.best == 0:
                return 0
        
        return int(self.best*2)

