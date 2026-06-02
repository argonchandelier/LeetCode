from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.seen = [False]*numCourses
        self.path = [False]*numCourses
        self.res = []
        mp = defaultdict(list)
        for course, prereq in prerequisites:
            mp[prereq].append(course)
        
        for c in range(numCourses):
            if self.seen[c] == True:
                continue
            #self.seen[c] = True

            def dfs(cur, i):
                self.path[cur] = True
                self.seen[cur] = True
                for nxt in mp[cur]:
                    if self.path[nxt] == True:
                        return False
                    if self.seen[nxt] == True:
                        continue
                    
                    res = dfs(nxt, i)
                    if not res:
                        return False
                self.res.append(cur)
                self.path[cur] = False
                return True
                
            if not dfs(c, len(self.res)):
                return []

        return self.res[::-1]