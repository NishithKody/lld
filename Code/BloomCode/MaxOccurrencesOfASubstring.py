class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        map = defaultdict(int)
        n = len(s)

        for i in range(0,n-minSize+1):
            wind = s[i:i+minSize]
            setVal = set(wind)
            if(len(setVal)>maxLetters):
                continue
            map[wind] = map[wind] + 1
        
        maxVal = 0
        if(len(map)>0):
            maxVal = max(map.values())

        return maxVal