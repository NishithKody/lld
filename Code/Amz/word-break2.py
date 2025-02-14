class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        res = []
        n = len(s)

        def util(i, val):

            if(i == n):
                res.append(' '.join(val))
                return
            
            for j in range(i,n):
                curWord = s[i:j+1]

                if(curWord in wordSet):
                    val.append(curWord)
                    util(j+1, val)
                    val.pop()

        util(0, [])
        return res
    