class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mp = {'+': lambda: stack[-2] + stack[-1],
              '-': lambda: stack[-2] - stack[-1], 
              '*': lambda: stack[-2] * stack[-1], 
              '/': lambda: int(stack[-2] / stack[-1])}
        
        for token in tokens:
            if token in mp:
                stack[-2] = mp[token]()
                stack.pop()
                continue
            stack.append(int(token))
        
        return stack[0]