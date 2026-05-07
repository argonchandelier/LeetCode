conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        s += 'I'
        res = 0
        for i in range(n):
            n = conv[s[i]]
            if n >= conv[s[i+1]]:
                res += n
                continue
            res -= n
        
        return res