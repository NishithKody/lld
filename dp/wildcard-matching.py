class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)

        def util(i,j):

            if(i<0 and j<0):
                return True
            if(i>=0 and j<0):
                return False
            if(i<0 and j>=0):
                for tmp in p[:j+1]:
                    if(tmp!='*'):
                        return False
                return True

            if(s[i]==p[j] or p[j]=='?'):
                return util(i-1, j-1)
            
            if(p[j]=='*'):
                return util(i-1,j) or util(i,j-1)
            
            return False
        
        res = util(n-1, m-1)
        return res
