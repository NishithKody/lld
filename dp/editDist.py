class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        def util(n,m):

            if(n<0):
                return m+1
            if(m<0):
                return n+1

            if(word1[n]==word2[m]):
                return  util(n-1,m-1)

            delChar = util(n-1,m) +1
            replaceChar = util(n-1, m-1)+1
            insertChar = util(n,m-1)+1

            return min(delChar,replaceChar,insertChar)
        
        res = util(n-1,m-1)
        return res
    
    # dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = []

        for i in range(n+1):
            val = [0]*(m+1)
            dp.append(val)
        
        for i in range(n+1):
            dp[i][0] = i
        
        for i in range(m+1):
            dp[0][i] = i

        for i in range(1,n+1):
            for j in range(1,m+1):

                if(word1[i-1]==word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delChar = dp[i-1][j] +1
                    replaceChar = dp[i-1][j-1]+1
                    insertChar = dp[i][j-1]+1

                    dp[i][j] = min(delChar,replaceChar,insertChar)

        return dp[n][m]