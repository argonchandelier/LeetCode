class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        n = len(digits)
        self.chars = ['']*n
        self.res = []
        
        def backtrack(i):
            if i == n:
                self.res.append(''.join(self.chars))
                return
            for c in mp[digits[i]]:
                self.chars[i] = c
                backtrack(i+1)
        backtrack(0)

        return self.res