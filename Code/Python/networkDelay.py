class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        t = 0
        minHeap = []
        visit = set()

        minHeap = [(0,k)]

        while(len(minHeap)>0):
            w1,n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2,w2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2,n2))
        
        return t if len(visit)==n else -1