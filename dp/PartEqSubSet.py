class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum +=i
        if(sum%2!=0):
            return False
        k = sum/2
        print('k',k)
        n = len(nums)
        
        def util(i,target):
            if(i<0):
                return False

            if(target == 0):
                print('target',target)
                return True
            
            dsel = util(i-1, target)
            sel = False
            if(nums[i]<=target):
                sel = util(i-1, target-nums[i])
            
            return dsel or sel
        
        res = util(n-1, k)
        return res

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum +=i
        if(sum%2!=0):
            return False
        k = sum//2

        n = len(nums)

        dp = []
        for i in range(n+1):
            val = [False] * (k+1)
            dp.append(val)
        
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1,k+1):
                dsel = dp[i-1][j]
                sel = False
                if(nums[i-1]<=j):
                    sel = dp[i-1][j-nums[i-1]]
                
                dp[i][j] = dsel or sel

        return dp[n][k]
