class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for i,val in enumerate(equations):
            a,b = val
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        res = []
        def util(src, target):
            if(src not in adj or target not in adj):
                return -1

            q = deque()
            visit = set()
            visit.add(src)
            q.append([src,1])

            while(len(q)>0):
                cur,w = q.popleft()
                if(cur == target):
                    return w

                for ngh, new_wt in adj[cur]:
                    if ngh not in visit:
                        q.append([ngh, w * new_wt])
                        visit.add(ngh)
            
            return -1
            
        for [start,end] in queries:
            val = util(start, end)
            res.append(val)
        
        return res
            