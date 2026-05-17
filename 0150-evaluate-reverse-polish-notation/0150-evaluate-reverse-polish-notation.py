class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        def plus():
            x = self.stack.pop()
            self.stack[-1] += x
        def minus():
            x = self.stack.pop()
            self.stack[-1] -= x
        def mult():
            x = self.stack.pop()
            self.stack[-1] *= x
        def div():
            x = self.stack.pop()
            self.stack[-1] = int(self.stack[-1] / x)
        mp = {'+': plus, '-': minus, '*': mult, '/': div}
        
        for token in tokens:
            if token in mp:
                mp[token]()
                continue
            self.stack.append(int(token))
        
        return self.stack[-1]