class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        goali = wordList.index(endWord)
        nwords = len(wordList)
        nletters = len(beginWord)
        seen = [False]*nwords
        cur = [beginWord]
        if beginWord in wordList:
            seen[wordList.index(beginWord)] = True

        res = 2
        while cur:
            nxt = []
            for w1 in cur:
                for i, w2 in enumerate(wordList):
                    if seen[i]:
                        continue
                    off = 0
                    for j in range(nletters):
                        if w1[j] == w2[j]:
                            continue
                        off += 1
                        if off > 1:
                            break
                    else:
                        if goali == i:
                            return res
                        seen[i] = True
                        nxt.append(w2)
            cur = nxt
            res += 1
        return 0

