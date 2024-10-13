class Solution:

    def isPal(self,s):
        l=0
        r=len(s)-1

        while(l<=r):
            rval = s[r]
            lval = s[l]

            if(rval!=lval):
                return False
            l=l+1
            r=r-1
            
        return True

    def shortestPalindrome(self, s: str) -> str:

        n=len(s)
        index = n
        for i in range(n, 0, -1):
            prefix = s[0:i]
            res = self.isPal(prefix)

            if(res == True):
                index = i
                break

        toAdd = s[index:]

        return toAdd[::-1]+s


        