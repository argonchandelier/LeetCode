class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        c0 = needle[0]
        for i in range(m-n+1):
            if haystack[i] == needle[0] and haystack[i:i+n] == needle:
                return i
        return -1
        