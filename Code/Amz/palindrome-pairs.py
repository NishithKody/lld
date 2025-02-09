class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        map = defaultdict(int)
        for i,word in enumerate(words):
            map[word] = i

        res = set()

        def isPal(s):
            if(s==s[::-1]):
                return True
            else:
                return  False

        for ind,word in enumerate(words):
            for i in range(len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                revPrefix = prefix[::-1]
                revSuffix = suffix[::-1]

                if(isPal(suffix) and revPrefix in map and map[revPrefix]!=ind):
                    res.add((ind, map[revPrefix]))

                if(isPal(prefix) and revSuffix in map and map[revSuffix]!=ind):
                    res.add((map[revSuffix], ind))
                
        return list(res)
