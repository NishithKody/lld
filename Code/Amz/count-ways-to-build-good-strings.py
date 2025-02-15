class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        mod = 10**9 + 7 

        def util(i):
            if i in dp:
                return dp[i]

            res = 0
            if(i>high):
                return res

            if(i>=low):
                res = res + 1
            
            addZeroVal = util(i+zero) 
            addOneVal = util(i+one) 
            res = (res + addZeroVal + addOneVal) % mod

            dp[i] = res 
            return res
        
        return util(0)
            