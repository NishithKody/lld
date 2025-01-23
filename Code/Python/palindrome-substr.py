class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):

            l=i
            r=i

            while(r<n and l>=0 and s[l]==s[r]):
                res = res + 1
                l = l - 1
                r = r + 1

            l=i
            r=i+1

            while(r<n and l>=0 and s[l]==s[r]):
                res = res + 1
                l = l -1
                r = r + 1
        
        return res
    