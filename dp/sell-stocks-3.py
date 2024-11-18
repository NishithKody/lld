class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        k=2

        def util(i, buy, j):
            if(i>=n):
                return 0
            
            if(j>=2):
                return 0

            if(buy == 1):
                buyStock = util(i+1, 0, j) - prices[i]
                skipBuy = util(i+1, 1, j)
                return max(buyStock, skipBuy)
            elif(buy == 0): # you have stock
                selStock = util(i+1, 1, j+1) + prices[i]
                skipSell = util(i+1, 0, j)
                return max(selStock, skipSell)

        res = util(0, 1, 0)
        return res
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        k=2

        dp = []
        for i in range(n+1):

            day_states = []
            for j in range(2):
                txn = [0] * (k+1)
                day_states.append(txn)
            dp.append(day_states)
        

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for j in range(k):
                    if(buy == 1):
                        buyStock = dp[i+1][0][j] - prices[i]
                        skipBuy = dp[i+1][1][j]
                        dp[i][buy][j] =  max(buyStock, skipBuy)
                    elif(buy == 0): 
                        selStock = dp[i+1][1][j+1] + prices[i]
                        skipSell = dp[i+1][0][j]
                        dp[i][buy][j] =  max(selStock, skipSell)

        return dp[0][1][0]
