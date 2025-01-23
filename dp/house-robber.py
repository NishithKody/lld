
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        def util(i):
            if(i<0):
                return 0
            
            #sel
            sel = util(i-2) + nums[i]
            #dsel
            dsel = util(i-1)

            return max(sel,dsel)

        res = util(n-1)
        return res


#at dp[i], it is the max till the ith index
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if(n==1):
            return nums[0]
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[1],dp[0])

        for i in range(2,n):
            sel = dp[i-2] + nums[i]
            dsel = dp[i-1]

            dp[i] = max(sel,dsel)

        return dp[n-1]
