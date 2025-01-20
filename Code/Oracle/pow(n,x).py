class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if(x==1 or x==0):
            return x

        def util(num, val):
            
            if(val == 0):
                return 1
            
            tmp = util(num, val//2) 
            tmp = tmp * tmp
            return tmp * num if val % 2 ==1 else tmp

        
        res = util(x,abs(n))
        return res if(n>0) else (1/res)
