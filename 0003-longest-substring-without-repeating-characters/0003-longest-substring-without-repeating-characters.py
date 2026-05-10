class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        res = 0
        cur = 0
        p1 = 0
        for p2, c in enumerate(s):
            cur += 1
            if c not in track:
                track.add(c)
                res = max(cur, res)
                continue
            while c != s[p1]:
                track.remove(s[p1])
                p1 += 1
                cur -= 1
            if p1 < p2:
                p1 += 1
                cur -= 1
        
        return res