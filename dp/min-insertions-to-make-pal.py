#find the longest palindrome substring, then subtract from the length

class Solution:
    def minInsertions(self, s: str) -> int:

        def longestPalindromeSubseq(s: str) -> int:
            n = len(s)
            r = s[::-1]

            dp = []
            
            for i in range(n+1):
                tmp = [0] * (n+1)
                dp.append(tmp)
            
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if(s[i-1] == r[j-1]):
                        dp[i][j] =  dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[n][n]
        
        lps = longestPalindromeSubseq(s)
        return len(s)-lps


class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)

        def util(i,j):

            if(i>=j):
                return 0
            
            if(s[i]==s[j]):
                return util(i+1,j-1) + 0
            else:
                return min(util(i+1,j), util(i, j-1))+1
        
        res = util(0,n-1)
        return res