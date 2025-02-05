class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        res = set()
        n = len(s)

        for ch in set(s):
            first = s.find(ch)
            last = s.rfind(ch)

            if(first<last):
                uniqueMid = set(s[first+1:last])

                for mid in uniqueMid:
                    res.add((ch, mid, ch))
            
        return len(res)


#not optimized
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        res = set()
        n = len(s)

        l = 0
        r = n-1

        for i in range(n):

            l = i+1
            r = n-1

            while(l<r):
                if(s[i]==s[r]):
                    res.add((s[i],s[l],s[r]))
                    l=l+1
                else:
                    r=r-1
        
        return len(res)

