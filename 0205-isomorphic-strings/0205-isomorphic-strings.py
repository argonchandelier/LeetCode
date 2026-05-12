class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smapt = {}
        tincl = set()
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            if cs not in smapt:
                if ct in tincl:
                    return False
                smapt[cs] = ct
                tincl.add(ct)
                continue
            if smapt[cs] != ct:
                return False
        
        return True
