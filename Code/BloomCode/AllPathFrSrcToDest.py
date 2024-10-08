class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i,edges in enumerate(graph):
            for edge in edges:
                adj[i].append(edge)
        
        print('adj',adj)
        target = n-1
        res = []

        def util(node,val):
            

            if(node==target):
                res.append(val.copy())
                return
            
            for ngh in adj[node]:
                val.append(ngh)
                util(ngh,val)
                val.pop()
        
        util(0,[0])
        return res