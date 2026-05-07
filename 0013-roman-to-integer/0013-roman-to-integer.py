conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            n = conv[s[i]]
            if n >= conv[s[i+1]]:
                res += n
                continue
            res -= n
        
        return res+conv[s[-1]]