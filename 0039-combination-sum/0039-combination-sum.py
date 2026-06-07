class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        n = len(candidates)
        def bt(csum, cur, mini):
            for i in range(mini, n):
                num = candidates[i]
                nsum = csum + num
                if nsum < target:
                    cur.append(num)
                    bt(nsum, cur, i)
                    cur.pop()
                    continue
                elif nsum > target:
                    return
                cur.append(num)
                self.res.append(cur[:])
                cur.pop()
                return
        bt(0, [], 0)
        return self.res