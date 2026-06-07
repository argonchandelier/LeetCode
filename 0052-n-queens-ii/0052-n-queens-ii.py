class Solution:
    def totalNQueens(self, n: int) -> int:
        pslopes = [False]*(2*n-1)
        nslopes = [False]*(2*n-1)
        goodCs = {i for i in range(n)}
        self.res = 0

        def bt(r):
            if r == n:
                self.res += 1
                return
            nval0 = n-1-r
            for c in list(goodCs):
                nval = nval0 + c
                if nslopes[nval]:
                    continue
                pval = r+c
                if pslopes[pval]:
                    continue
                pslopes[pval] = True
                nslopes[nval] = True
                goodCs.remove(c)
                bt(r+1)
                goodCs.add(c)
                pslopes[pval] = False
                nslopes[nval] = False
        bt(0)
        return self.res



