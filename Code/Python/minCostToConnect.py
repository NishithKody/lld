class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        cost = 0
        minheap = [(0,0)]
        visit = set()

        while(len(visit)<n):
            dist, i  = heapq.heappop(minheap)
            if(i in visit):
                continue
            
            visit.add(i)
            
            cost = cost + dist

            x1,y1 = points[i]

            for j in range(n):
                if j in visit:
                    continue
                x2, y2 = points[j]
                tmp = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(minheap, (tmp,j))

        return cost