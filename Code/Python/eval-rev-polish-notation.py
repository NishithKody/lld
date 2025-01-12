class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        if(len(tokens)==1):
            return int(tokens[0])

        for val in tokens:
            if(val=='-'):
                b = int(stk.pop())
                a = int(stk.pop())
                res = a - b
                stk.append(res)
            elif(val == '+'):
                b = int(stk.pop())
                a = int(stk.pop())
                res = a + b
                stk.append(res)
            elif(val == '*'):
                b = int(stk.pop())
                a = int(stk.pop())
                res = a * b
                stk.append(res)
            elif(val == '/'):
                b = int(stk.pop())
                a = int(stk.pop())
                res = a / b
                stk.append(res)
            else:
                stk.append(val)
            
            print('stk',stk)
        return int(stk[0])
    