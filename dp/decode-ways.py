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