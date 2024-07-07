class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        global res
        res = 0
        n = len(nums)

        def util(i, total):
            global res
            if(total == target and i == n):
                res = res +1
            if(i>=n):
                return
            
            val = nums[i]
            util(i+1, total+val)
            util(i+1, total-val)
        
        util(0,0)
        return res