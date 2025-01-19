class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []

        for val in s:
            if(val=='('):
                stk.append(val)
            elif(val==')'):
                tmp=""
                while(stk[-1]!='('):
                    tmp = tmp + stk.pop()[::-1]

                stk.pop()
                stk.append(tmp)
            else:
                stk.append(val)

        res = ""
        
        for val in stk:
            res = res + val
            
        return res
