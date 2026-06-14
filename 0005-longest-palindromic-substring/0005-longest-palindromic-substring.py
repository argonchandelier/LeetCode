class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 1
        mxs = s[0]
        n = len(s)
        for i1c in range(n):
            for c in range(2):
                i1, i2 = i1c, i1c + c
                c -= 1
                while i1 >= 0 and i2 < n:
                    if s[i1] != s[i2]:
                        break
                    c += 2
                    if c > mx:
                        mx = c
                        mxs = s[i1:i2+1]
                    i1 -= 1
                    i2 += 1
        return mxs
        