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

                dp[i][j] = dsel+sel

        return dp[n][amount]
