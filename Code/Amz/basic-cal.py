class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        sign = 1
        res = 0

        n=len(s)
        i = 0
        val = 0
        
        for ch in s:
            if(ch.isdigit()):
                val = val*10 + int(ch) 
            elif(ch in ['+','-']):
                res += val * sign
                sign = 1 if ch =='+' else -1
                val = 0
            elif(ch == '('):
                stk.append(res)
                stk.append(sign)
                sign = 1
                res = 0
            elif(ch==')'):
                res += val*sign

                prevSign = stk.pop()
                prevRes = stk.pop()

                res = res * prevSign
                res = res + prevRes
                
                val = 0

        return res + val * sign
                