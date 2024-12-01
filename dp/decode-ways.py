class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        def util(i):
            
            if(i==n):
                return 1
            
            if(s[i] == '0'):
                return 0

            single = 0 
            double = 0

            single = util(i+1) 
            
            if(i+1 < n and s[i+1]<='6'):
                double = util(i+2) 

            return single + double

        res = util(0)
        return res
    

    #dp
    class Solution:
        def numDecodings(self, s: str) -> int:
            
            n = len(s)
            dp = [0] * (n+1)

            dp[n] = 1

            for i in range(n-1, -1, -1):

                if(s[i] == '0'):
                    continue
                
                single = 0 
                double = 0

                single = dp[i+1] 
                
                if(i+1 < n and 10 <= int(s[i:i+2]) <=26):
                    double = dp[i+2]
                            
                dp[i] =  single + double

            return dp[0]
