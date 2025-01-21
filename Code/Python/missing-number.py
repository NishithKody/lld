class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = ((n+1)*n)//2

        for n in nums:
            res = res - n

        return res 
        