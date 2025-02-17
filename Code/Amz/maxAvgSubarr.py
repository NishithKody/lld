class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(k>len(nums)):
            return 0
        n = len(nums)
        res = -math.inf
        l = 0
        total = 0

        for r in range(n):
            rval = nums[r]
            total += rval

            if(r>=k-1):
                avg = total/k
                res=max(res,avg)
                lval = nums[l]
                total -= lval
                l=l+1
            
        return res
    