class Node:
    def __init__(self, name=""):
        self.name = name
        self.ratios = {}
    
    def add(self, node, ratio):
        self.ratios[node] = ratio
        node.ratios[self] = 1/ratio

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}
        for i, eq in enumerate(equations):
            ratio = values[i]
            if eq[0] in nodes: n1 = nodes[eq[0]]
            else: n1 = Node(eq[0]); nodes[eq[0]] = n1
            if eq[1] in nodes: n2 = nodes[eq[1]]
            else: n2 = Node(eq[1]); nodes[eq[1]] = n2
            n1.add(n2, ratio)
        
        res = []
        for qn, qd in queries:
            if qn not in nodes or qd not in nodes:
                res.append(-1.0)
                continue
            if qn == qd:
                res.append(1.0)
                continue
            nn, nd = nodes[qn], nodes[qd]
            if nd in nn.ratios:
                res.append(nn.ratios[nd])
                continue
            
            seen = {nn: 1}
            cur = [nn]
            while cur:
                curnode = cur.pop()
                ratio1 = seen[curnode]
                for n2, ratio2 in curnode.ratios.items():
                    if ratio2 < 0:
                        res.append(-1.0)
                        break
                    if n2 in seen:
                        continue
                    newratio = ratio1*ratio2
                    nn.add(n2, newratio)
                    if n2 is nd:
                        res.append(newratio)
                        break
                    cur.append(n2)
                    seen[n2] = newratio
                else:
                    continue
                break
            else:
                nn.add(nd, -1.0)
                res.append(-1.0)
        
        return res


