class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        chars = set()
        for word in wordDict:
            for c in word:
                if c not in chars:
                    chars.add(c)
        for c in s:
            if c not in chars:
                return False
        inds = [0]
        seen = {0}
        n = len(s)
        mxwl = max(len(word) for word in wordDict)
        mx = 0
        while inds:
            i = inds.pop()
            if i+mxwl <= mx:
                continue
            for word in wordDict:
                lw = len(word)
                if lw+i > n:
                    continue
                for j in range(lw):
                    if word[j] != s[i+j]:
                        break
                else:
                    ni = lw+i
                    if ni > n:
                        continue
                    if ni == n:
                        return True
                    inds.append(ni)
                    seen.add(ni)
                    mx = max(mx, ni)
        return False
                    