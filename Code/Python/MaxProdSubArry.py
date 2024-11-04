# keep track of both the positive and negative prod

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minSum = nums[0]
        maxSum = nums[0]
        res = nums[0]

        for i,val in enumerate(nums[1:]):
            tmpMax = maxSum
            tmpMin = minSum

            maxSum = max(val, val*tmpMax, val*tmpMin)
            minSum = min(val, val*tmpMax, val*tmpMin)
            res = max(res, maxSum)

            print('max,min,res',maxSum,minSum,res)
        
        return res