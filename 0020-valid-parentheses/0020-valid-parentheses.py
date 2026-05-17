class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in mp:
                stack.append(c)
                continue
            if stack and mp[stack[-1]] == c:
                stack.pop()
                continue
            return False
        return False if stack else True