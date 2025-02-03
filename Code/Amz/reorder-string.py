class Solution:
    def reorganizeString(self, s: str) -> str:
        map = defaultdict(int)
        maxHeap = []
        res = ""

        for val in s:
            map[val] += 1
        
        for key,val in map.items():
            heapq.heappush(maxHeap, (-val, key))
        
        while(len(maxHeap)>=2):
            val1, key1 = heapq.heappop(maxHeap)
            val2, key2 = heapq.heappop(maxHeap)
            val1= -val1
            val2= -val2

            res = res+key1+key2
            val1 = val1 -1
            val2 = val2 -1
            if(val1>0):
                heapq.heappush(maxHeap, (-val1, key1))

            if(val2>0):
                heapq.heappush(maxHeap, (-val2, key2))

        while(maxHeap):
            val,key = heapq.heappop(maxHeap)
            val = -val

            if(val>=2):
                return ""
            else:
                res = res + key
        
        return res
                
