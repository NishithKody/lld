class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        res = 0
        n = len(coins)

        def util(i,val):
            
            if(val==0):
                return 0
            if(i<0 or val<0):
                return float('inf')
            
            dsel = util(i-1,val)
            sel = float('inf')

            if(coins[i]<=val):
                sel = util(i, val-coins[i]) + 1

            return min(sel,dsel)
        
        res = util(n-1,amount)
        
        return res if res!=float('inf') else -1
    

    class Solution:
    
        def coinChange(self, coins: List[int], amount: int) -> int:
            
            n = len(coins)
            dp = []
            
            for i in range(n+1):
                val = [float('inf')] * (amount+1)
                dp.append(val)

            for i in range(n+1):
                dp[i][0] = 0 

            for i in range(1,n+1):
                for j in range(1,amount+1):
                    dsel = dp[i-1][j]
                    sel = float('inf')

                    if(coins[i-1]<=j):
                            sel = dp[i][j-coins[i-1]] + 1
                    dp[i][j] = min(sel,dsel)

            return dp[n][amount] if dp[n][amount] != float('inf') else -1