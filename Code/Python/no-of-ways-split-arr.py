class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = 0 
        n = len(nums)
        for val in nums:
            total += val
        
        res = 0
        curTotal = 0
        for i in range(n-1):
            curTotal += nums[i]
            rem = total - curTotal
            # print('cur,rem',curTotal,rem)

            if(curTotal >= rem):
                res += 1
        
        return res