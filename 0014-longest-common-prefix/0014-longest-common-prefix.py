class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(len(s) for s in strs)
        m = len(strs)
        l = 0
        for i in range(n):
            c0 = strs[0][i]
            for j in range(1, m):
                if strs[j][i] != c0:
                    break
            else:
                l += 1
                continue
            break
        
        return strs[0][:l]
        