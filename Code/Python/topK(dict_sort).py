class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        res = []

        for i in nums:
            if( i in map.keys()):
                map[i] = map[i] + 1
            else:
                map[i] = 1
        
        
        map = sorted(map.items(), key=lambda val:val[1],reverse=True)

        count = 0
        while(count<k):
            res.append(map[count][0])
            count = count +1
        
        return res