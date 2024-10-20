class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)

        def util(i,val):
            if(i==n):
                res.append(" ".join(val))
                return
            
            for j in range(i,n):
                tmp = s[i:j+1]
                for word in wordDict:
                    if(tmp==word):
                        val.append(word)
                        util(j+1,val)
                        val.pop()
    
        util(0,[])
        return res