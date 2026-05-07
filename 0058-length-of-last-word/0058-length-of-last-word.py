class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        s = s.rstrip()
        for c in s:
            res += 1
            if c == ' ':
                res = 0
        return res