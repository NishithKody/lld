class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def util(i,target):

            if(i<0 or target<0):
                return 0

            if(target == 0):
                return 1

            dsel = util(i-1,target)
            sel = 0
            if(coins[i]<=target):
                sel = util(i, target-coins[i])
            
            return dsel + sel
        
        res = util(n-1,amount)
        return res

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = []
        for i in range(n+1):
            val = [0] * (amount+1)
            dp.append(val)
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(1,amount+1):

                dsel = dp[i-1][j]
                sel = 0
                if(coins[i-1]<=j):
                    sel = dp[i][j-coins[i-1]]
                
                dp[i][j] = dsel + sel

        return dp[n][amount]