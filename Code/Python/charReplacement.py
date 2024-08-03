class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0
        l = 0

        for r in range(0,len(s)):

            if(s[r] in map.keys()):
                map[s[r]] = map[s[r]] +1
            else:
                map[s[r]] = 1
            
            winLen = r - l +1
            curMax = max(map.values())

            if(winLen - curMax >k):
                rmVal = s[l]
                map[rmVal] = map[rmVal]-1
                l = l +1

            if((r-l+1)>res):
                res = r - l +1

        return res

        