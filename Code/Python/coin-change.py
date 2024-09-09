class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        def util(i,target):
            if(target==0):
                return 0
            
            if(target<0 or i<0):
                return float('inf')

            dsel = util(i-1,target)
            sel = float('inf')

            if(coins[i]<=target):
                val = target - coins[i]
                sel = util(i,val) +1
            return min(dsel,sel)
        
        finalRes = util(n-1,amount)
        if(finalRes == float('inf')):
            return -1
        else:
            return finalRes
    

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [] 
        for i in range(n+1):
            val = [float('inf')] * (amount+1)
            dp.append(val)
        

        for i in range(n+1):
            dp[i][0]=0
        
        print('init dp',dp)
        
        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]

                if(coins[i-1]<=j):
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i-1]] + 1)

        print('fin dp',dp)
        return dp[n][amount] if dp[n][amount] != float('inf') else -1


        