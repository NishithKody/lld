# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        def util(count, val):
            if(val==0):
                return 1
            
            if(val<0 or count<=0):
                return 0
            
            tmp = 0
            for i in range(1,k+1):
                zx = util(count-1, val - i)
                tmp += zx
            
            return  tmp
        
        res = util(n,target)
        return res % (10**9 + 7)
    

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        dp = []
        for i in range(n+1):
            tmp = [0]*(target+1)
            dp.append(tmp)

        # it is not possible to get a target of 0 if there are no dice
        # for i in range(n+1):
        #     dp[i][0] = 1

        dp[0][0] =1

        for i in range(1,n+1):
            for j in range(1,target+1):

                tmp = 0
                for b in range(1,k+1):
                    if(j-b>=0):
                        zx = dp[i-1][j-b]
                        tmp += zx
                
                dp[i][j]=tmp
        
        return dp[n][target] % (10**9 + 7)
                