class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n= len(prices)

        def util(i,buy):

            if(i>=n):
                return 0

            if(buy==1):
                sel = util(i+1,0) - prices[i]
                dsel = util(i+1,1)
                return max(sel,dsel)
            else:
                sel = util(i+2,1) + prices[i]
                dsel = util(i+1,0)
                return max(sel,dsel)

        res = util(0,1)
        return res

        