from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        tmap = defaultdict(int)
        for c in t:
            tmap[c] += 1

        smap = defaultdict(int)
        emap = defaultdict(int)
        excess = 0
        mn = float('inf')
        left = 0
        while s[left] not in tmap:
            left += 1
            if left == m:
                return ""
        right = left

        while left < m:
            while smap != tmap:
                if right == m:
                    return s[res[0]:res[1]] if mn < float('inf') else ""
                cr = s[right]
                if cr not in tmap:
                    right += 1
                    continue
                if tmap[cr] == smap[cr]:
                    excess += 1
                    emap[cr] += 1
                else:
                    smap[cr] += 1
                right += 1
            if right-left < mn:
                mn = right-left
                res = [left, right]
            cl = s[left]
            if emap[cl] > 0: # The 2nd loop will be skipped next time if this happens
                emap[cl] -= 1
                excess -= 1
            else:
                smap[cl] -= 1

            left += 1
            while left < m and s[left] not in tmap:
                left += 1
        
        return s[res[0]:res[1]] if mn < float('inf') else ""


