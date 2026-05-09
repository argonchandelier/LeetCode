allowed = {chr(i) for i in range(ord('a'), ord('z')+1)} | {chr(i) for i in range(ord('0'), ord('9')+1)}

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            while p1 < len(s) and s[p1] not in allowed:
                p1 += 1
            while p2 >= 0 and s[p2] not in allowed:
                p2 -= 1
            if p1 >= p2:
                return True
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True