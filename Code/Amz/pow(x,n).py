class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def util(power):
            if(power==0):
                return 1

            if(power==1):
                return x
            
            val = util(power//2)

            return val*val if power%2==0 else val*val*x

        return util(abs(n)) if n>0 else 1/util(abs(n))
