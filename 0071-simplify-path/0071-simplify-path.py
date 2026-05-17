class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['']
        cur = []
        for c in path[1:]+'/':
            if c != '/':
                cur.append(c)
                continue
            if len(cur) == 0:
                continue
            if cur == ['.']:
                cur = []
                continue
            if cur == ['.', '.']:
                if len(stack) > 1:
                    stack.pop()
                cur = []
                continue
            stack.append(''.join(cur))
            cur = []
        
        return '/'.join(stack) if len(stack) > 1 else '/'
            
                
