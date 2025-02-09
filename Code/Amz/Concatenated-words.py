class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        wordset = set(words)

        def util(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if((prefix in wordset and suffix in wordset) or
                    (prefix in wordset and util(suffix))):
                    return True        

        for word in words:
            if(util(word)):
                res.append(word)
        
        return res
        