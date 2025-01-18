class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)

        for val in nums:
            map[val] = map[val] + 1
        
        heap = []

        for [key,val] in map.items():
            heapq.heappush(heap, (val, key))

            if(len(heap)>k):
                heapq.heappop(heap)
        
        res = []
        while(heap):
            [val,key] = heapq.heappop(heap)
            res.append(key)
        
        return res
    