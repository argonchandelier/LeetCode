from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.seen = [False]*numCourses
        self.path = [False]*numCourses
        mp = defaultdict(list)
        for course, prereq in prerequisites:
            mp[course].append(prereq)
        
        for c in range(numCourses):
            if self.seen[c] == True:
                continue
            self.seen[c] = True

            def dfs(cur):
                self.path[cur] = True
                self.seen[cur] = True
                for nxt in mp[cur]:
                    if self.path[nxt] == True:
                        return False
                    if self.seen[nxt] == True:
                        continue
                    res = dfs(nxt)
                    if not res:
                        return False
                self.path[cur] = False
                return True
            if not dfs(c):
                return False

        return True
        