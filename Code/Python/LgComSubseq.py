#This is based on comparision of strings, consider the index and then compare


class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        def util(ind1, ind2):
            if(ind1<0 or ind2<0):
                return 0
            
            if(t1[ind1]==t2[ind2]):
                return 1 + util(ind1-1, ind2-1)

            return max(util(ind1-1,ind2),util(ind1,ind2-1))
        
        res = util(len(t1)-1, len(t2)-1)

        return res
    
#Tabulation
#copy the base case
#shift the index
#copy the recur

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        n = len(t1)
        m = len(t2)
        dp = []
        for i in range(n+1):
            val = [0] * (m+1)
            dp.append(val)
        
        # for i in range(0,n+1):
        #     dp[i][0] = 0
        
        # for i in range(0,m+1):
        #     dp[0][i] = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(t1[i-1]==t2[j-1]):
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        print(dp)
        return dp[n][m]

        
        