class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def util(i,j):
            if(i>=n and j>=m):
                return True

            if(j>=m):
                return False
            
            match = i<n and (s[i] == p[j] or p[j] == '.')

            if(j+1<m and p[j+1]=='*'):
                skip_star = util(i, j+2)
                sel_star = match and util(i+1, j)
                return skip_star or sel_star
            else:
                return match and util(i+1, j+1)

        res = util(0,0)
        return res
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = []
        for i in range(n+1):
            tmp = [False] * (m+1)
            dp.append(tmp)

        dp[n][m] = True
        
        for i in range(n, -1, -1):
            for j in range(m-1, -1, -1):

                match = i<n and (s[i] == p[j] or p[j] == '.')

                if(j+1<m and p[j+1]=='*'):
                    skip_star = dp[i][j+2]
                    sel_star = match and dp[i+1][j]
                    dp[i][j] =  skip_star or sel_star
                else:
                    dp[i][j] =  match and dp[i+1][j+1]

        return dp[0][0]
