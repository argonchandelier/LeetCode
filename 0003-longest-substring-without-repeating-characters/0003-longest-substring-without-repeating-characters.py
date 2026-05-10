class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        cur = 0
        p1 = 0
        for c in s:
            cur += 1
            if c not in mp:
                mp[c] = 1
            else:
                mp[c] += 1
                while mp[c] > 1:
                    mp[s[p1]] -= 1
                    p1 += 1
                    cur -= 1
            res = max(cur, res)
        
        return res