class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        map = {}
        res = []
        n = len(barcodes)

        for i in barcodes:
            map[i]=map.get(i,0)+1
        
        lst = list(map.items())
        # print('list',lst)
        heap = []

        for [key,val] in lst:
            heapq.heappush(heap,(-val,key))

        while(len(heap)>0):
            cur = heapq.heappop(heap)
            if(len(res)>0 and cur[1]==res[-1]):
                nxtCur = heapq.heappop(heap)
                heapq.heappush(heap,cur)
                cur=nxtCur

            [val,key] = cur
            val = -val
            # print('val,key',val,key)
            res.append(key)
            val = val -1
            if(val !=0):
                heapq.heappush(heap,(-val,key))

        return res

