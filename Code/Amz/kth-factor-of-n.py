class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        res = -1
        cnt = 0

        for fct in range(1,n+1):
            if(n%fct == 0):
                cnt = cnt+1
                if(cnt==k):
                    return fct
        
        return res
    
    