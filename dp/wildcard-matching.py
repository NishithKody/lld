class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)

        def util(i,j):

            if(i<0 and j<0):
                return True
            if(i>=0 and j<0):
                return False
            if(i<0 and j>=0):
                for tmp in p[:j+1]:
                    if(tmp!='*'):
                        return False
                return True

            if(s[i]==p[j] or p[j]=='?'):
                return util(i-1, j-1)
            
            if(p[j]=='*'):
                return util(i-1,j) or util(i,j-1)
            
            return False
        
        res = util(n-1, m-1)
        return res


#DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)

        dp = []
        for i in range(n+1):
            val = [False] * (m+1)
            dp.append(val)
        
        dp[0][0] = True

        for i in range(1,n+1):
            dp[i][0] = False
        
        for j in range(1, m+1):
            dp[0][j] = True
            for k in range(1,j+1):
                if(p[k-1]!='*'):
                    dp[0][j] = False
        
        for i in range(1,n+1):
            for j in range(1,m+1):
            
                if(s[i-1]==p[j-1] or p[j-1]=='?'):
                    dp[i][j] = dp[i-1][j-1]
                
                elif(p[j-1]=='*'):
                    dp[i][j] =  dp[i-1][j] or dp[i][j-1]
                
                else:
                    dp[i][j] = False
        
        return dp[n][m]
