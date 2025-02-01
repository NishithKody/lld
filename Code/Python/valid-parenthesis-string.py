class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)

        def util(i, opn):
            if(i==n):
                if(opn==0):
                    return True
                else:
                    return False
            
            if(opn<0):
                return False
            
            if(s[i]=='('):
                return util(i+1, opn+1)
            elif(s[i]==')'):
                return util(i+1, opn-1)
            else:
                leftbrac = util(i+1, opn+1)
                nobrac = util(i+1, opn)
                rightbrac = util(i+1, opn -1)

                return leftbrac or nobrac or rightbrac
        
        res = util(0,0)
        return res
    