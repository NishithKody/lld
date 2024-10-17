class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)

        def util(i,j):

            if(i>=j):
                return 0
            
            if(s[i]==s[j]):
                return util(i+1,j-1) + 0
            else:
                return min(util(i+1,j), util(i, j-1))+1
        
        res = util(0,n-1)
        return res