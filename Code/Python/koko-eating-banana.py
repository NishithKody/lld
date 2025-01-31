class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles) 
        res = r
        while(l<=r):
            mid = (l+r)//2
            val = 0

            for p in piles:
                tmp = math.ceil(p/mid)
                val += tmp
            
            if(val<=h):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        
        return res
