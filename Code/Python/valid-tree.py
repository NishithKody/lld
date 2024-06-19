class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {}
        for i in range(n):
            adj[i] = []

        for [f,s] in edges:
            adj[f].append(s)
            adj[s].append(f)
        
        visit = set()

        def util(node,prev):

            if node in visit:
                return False
            
            visit.add(node)
            for ngh in adj[node]:
                if(ngh == prev):
                    continue
                val = util(ngh, node)
                if(val == False):
                    return False

            return True
        
        val = util(0,-1)
        if(val==False):
            return False
        
        if(len(visit)!=n):
            return False
        
        return True
