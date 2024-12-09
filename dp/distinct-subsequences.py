class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        def util(i,j):
            
            if(j==m):
                return 1
            
            if(i>=n or j>m):
                return 0
            
            if(s[i] == t[j]):
                sel = util(i+1, j+1)
                dsel = util(i+1, j)
                return sel + dsel
            else:
                return util(i+1, j)


        res = util(0,0)
        return res

#dp

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = []
        for i in range(n+1):
            val = [0] * (m+1)
            dp.append(val)
        
        for i in range(n+1):
            dp[i][m] = 1

        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1 , -1):
        
                if(s[i] == t[j]):
                    sel = dp[i+1][j+1]
                    dsel = dp[i+1][j]
                    dp[i][j] = sel + dsel
                else:
                    dp[i][j] =  dp[i+1][j]
        
        return dp[0][0]
    