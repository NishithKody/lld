class Solution:
    def decodeString(self, s: str) -> str:
        num_stk = []
        alp_stk = []

        i=0
        while(i<len(s)):
            val = s[i]

            if(val>='0' and val<='9'):
                temp = ""
                while(val>='0' and val<='9'):
                    temp = temp + val
                    i = i  + 1
                    val = s[i]
                    
                num_stk.append(int(temp))
                continue
            
            elif(val==']'):
                num = num_stk.pop()

                ch = ""
                while(alp_stk[-1]!='['):
                    ch = alp_stk.pop() + ch
                
                alp_stk.pop()
                mul = ch * int(num)
                alp_stk.append(mul)
            
            else:
                alp_stk.append(val)
            i=i+1

        return ''.join(alp_stk)
