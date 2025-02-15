class Solution:
    def calculate(self, s: str) -> int:
        stk =  []
        sign = '+'
        n = len(s)
        curDigit = 0

        # 3+2*2+1
        for i,char in enumerate(s):

            if(char.isdigit()):
                curDigit = curDigit * 10 + int(char)
            
            if(char in ['+','-','*','/'] or i==n-1):
                if(sign == '+'):
                    stk.append(curDigit)
                elif(sign == '-'):
                    stk.append(-curDigit)
                elif(sign == '*'):
                    #add
                    val = curDigit * stk.pop()
                    stk.append(val)
                elif(sign == '/'):
                    #add
                    val = stk.pop() / curDigit  
                    stk.append(int(val))
                
                curDigit = 0
                sign = char
        
        res = 0
        while stk:
            res = res + stk.pop()
        
        return res
    