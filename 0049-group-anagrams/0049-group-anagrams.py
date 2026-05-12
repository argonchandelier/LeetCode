class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = []
        counterset = set()
        res = []
        for s in strs:
            c = [0]*26
            for ch in s:
                c[ord(ch)-ord('a')] += 1
            c = tuple(c)

            if c in counterset:
                i = counters.index(c)
                res[i].append(s)
            else:
                res.append([s])
                counters.append(c)
                counterset.add(c)
        
        return res
