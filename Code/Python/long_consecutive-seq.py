class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0

        for num in nums:
            val = num
            if(val -1 not in s):
                temp = 1
                while(val+1 in s):
                    temp = temp +1
                    val = val+1
                if(temp>res):
                    res=temp
        
        return res
