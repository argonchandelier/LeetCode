class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Are all words unique? maybe make a hashmap from word to set
        m, mm, n = len(words), len(words[0]), len(s)
        mmm = m*mm
        mp = {}
        res = []
        for i, word in enumerate(words):
            if word in mp:
                mp[word] += 1
                continue
            mp[word] = 1
        
        for i in range(n-mmm+1):
            mpNew = {}
            for j in range(i, i+mmm, mm):
                ss = s[j:j+mm]
                if ss not in mp:
                    break
                if ss in mpNew:
                    mpNew[ss] += 1
                    continue
                mpNew[ss] = 1
            else:
                if mpNew == mp:
                    res.append(i)
        
        return res
