class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        def util(i,j):
            
            if(j==m):
                return 1
            
            if(i>=n or j>m):
                return 0
            
            if(s[i] == t[j]):
                sel = util(i+1, j+1)
                dsel = util(i+1, j)
                return sel + dsel
            else:
                return util(i+1, j)


        res = util(0,0)
        return res
    