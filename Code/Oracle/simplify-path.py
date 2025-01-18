class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        res = "/"
        vals = path.split('/')

        for val in vals:
            if(len(val)==0):
                continue
            
            if(val == '..'):
                if(len(stk)>0):
                    stk.pop()
            elif(val == '.'):
                continue
            else:
                stk.append(val)
        
        stk_len = len(stk)
        for i,val in enumerate(stk):
            if(i==stk_len-1):
                res = res+val
            else:
                res = res+ val+ '/'

        return res
        
