class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        goali = wordList.index(endWord)
        nwords = len(wordList)
        nletters = len(beginWord)
        seen = [False]*nwords
        seen2 = [False]*nwords
        cur = {beginWord}
        cur2 = {endWord}
        if beginWord in wordList:
            seen[wordList.index(beginWord)] = True

        res = 2
        while cur and cur2:
            if len(cur) > len(cur2):
                cur2, cur = cur, cur2
                seen2, seen = seen, seen2
            nxt = set()
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
                        if w2 in cur2:
                            return res
                        seen[i] = True
                        nxt.add(w2)
            cur = nxt
            res += 1
        return 0

