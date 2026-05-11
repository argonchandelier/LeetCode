class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, mm, n = len(words), len(words[0]), len(s)
        mmm = m*mm
        mp = {}
        #set0 = set()
        res = []
        for i, word in enumerate(words):
            if word in mp:
                mp[word] += 1
                continue
            mp[word] = 1
            #set0.add(word[0])
        
        for offset in range(mm):
            mpNew = {}
            count = 0
            for j in range(offset, n-mm+1, mm):
                ss = s[j:j+mm]
                if ss not in mp: # ss[0] not in set0 or 
                    mpNew = {}
                    count = 0
                    continue
                count += 1
                if ss in mpNew:
                    mpNew[ss] += 1
                else:
                    mpNew[ss] = 1
                if mpNew == mp:
                    res.append(j-mmm+mm)
                if count == m:
                    count -= 1
                    word = s[j-mmm+mm:j+2*mm-mmm]
                    mpNew[word] -= 1
        
        return res
