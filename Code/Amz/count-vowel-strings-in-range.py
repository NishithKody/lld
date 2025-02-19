class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        soFar = 0
        count = []
        count.append(0)
        wordSet = set(['a','e','i','o','u'])

        for wd in words:
            if(wd[0] in wordSet and wd[-1] in wordSet):
                soFar += 1
            count.append(soFar)

        res = []

        for [start,end] in queries:
            endVal = count[end+1]
            startVal = count[start]
            res.append(endVal - startVal)
        return res
                    