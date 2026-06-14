class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if l != m+n:
            return False
        stored = {(-1,-1)}
        for k, c in enumerate(s3):
            newstored = set()
            for i, j in stored:
                i1, j1 = i+1, j+1
                if j1 < n and c == s2[j1]:
                    nw = (i, j1)
                    if nw not in newstored: # if not newstored or newstored[-1] != nw
                        newstored.add(nw)
                if i1 < m and c == s1[i1]:
                    newstored.add((i1, j))
            stored = newstored
            if not stored:
                return False
        return True
