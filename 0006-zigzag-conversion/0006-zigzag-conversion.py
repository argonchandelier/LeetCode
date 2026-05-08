class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]

        row, dr = 0, 1
        switch = {0, numRows-1}
        for i, c in enumerate(s):
            res[row].append(c)
            row += dr
            if row in switch:
                dr *= -1

        return ''.join([''.join(st) for st in res])            
