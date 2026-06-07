class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.valid = [None]*2*n
        self.res = []
        
        def bt(exl, lleft, i):
            if i == 2*n:
                self.res.append(''.join(self.valid))
                return
            if lleft > 0:
                self.valid[i] = '('
                bt(exl+1, lleft-1, i+1)
            if exl > 0:
                self.valid[i] = ')'
                bt(exl-1, lleft, i+1)
        bt(0, n, 0)
        return self.res