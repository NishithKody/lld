class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)

        def util(i,j):

            if(j==m):
                return i==n
            
            match = (i<n and (s[i]==p[j] or p[j]=='.'))

            if(j+1<m and p[j+1]=='*'):
                return util(i,j+2) or (match and util(i+1,j))
            else:
                if(match):
                    return util(i+1, j+1)
            
            return False
        
        res = util(0,0)
        return res


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def util(i,j):
            if(i>=n and j>=m):
                return True

            if(j>=m):
                return False
            
            match = i<n and (s[i] == p[j] or p[j] == '.')

            if(j+1<m and p[j+1]=='*'):
                skip_star = util(i, j+2)
                sel_star = match and util(i+1, j)
                return skip_star or sel_star
            else:
                return match and util(i+1, j+1)

        res = util(0,0)
        return res