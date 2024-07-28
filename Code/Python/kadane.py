class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = 0
        globalMax = -math.inf

        for i in nums:
            localMax = max(i, localMax + i)
            globalMax = max(globalMax, localMax)
        
        return globalMax