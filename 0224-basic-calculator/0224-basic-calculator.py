class Solution:
    def calculate(self, s: str) -> int:
        stack = [0] # stack[-1] is working stack
        opStack = [1] # 1 or -1 for each layer
        cur = [] # list of digit chars
        s = s.replace(" ", "")
        for c in s:
            if c not in {'(', ')', '+', '-'}:
                cur.append(c)
                continue

            if cur:
                stack[-1] += opStack[-1]*int(''.join(cur))
                cur = []
            if c == "(":
                stack.append(0)
                opStack.append(1)
                # minus case: ?
            elif c == ")":
                stack[-2] += opStack[-2]*stack[-1]
                stack.pop()
                opStack.pop()
                opStack[-1] = 1
            elif c == "+":
                opStack[-1] = 1
            elif c == '-':
                opStack[-1] = -1

        if cur:
            stack[0] += opStack[0]*int(''.join(cur))
        return stack[0]

