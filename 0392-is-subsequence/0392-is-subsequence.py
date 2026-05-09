class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        if m == 0:
            return True
        p1, c1 = 0, s[0]
        for p2, c2 in enumerate(t):
            if c1 != c2:
                continue
            p1 += 1
            if p1 == m:
                return True
            c1 = s[p1]
        
        return False
