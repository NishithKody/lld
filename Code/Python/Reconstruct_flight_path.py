from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for [start, end] in tickets:
            adj[start].append(end)
            
        res = []

        for key in adj.keys():
            adj[key].sort(reverse=True)

        def util(node):

            while(adj[node]):
                rem_val = adj[node].pop()
                util(rem_val)
                
            res.append(node)
        
        util("JFK")

        return res[::-1]
