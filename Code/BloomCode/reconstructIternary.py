from collections import deque, defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)  # Using deque for fast pop operations

        # Build graph: adj list with reversed sorted destinations for efficient pop
        for start, end in sorted(tickets, reverse=True):
            adj[start].append(end)

        res = []

        def dfs(node):
            while adj[node]:
                next_node = adj[node].pop()  # Efficiently pop the last element
                dfs(next_node)
            res.append(node)

        dfs("JFK")

        return res[::-1]  # Reverse the result to get the correct order
