class Solution:
    def frequencySort(self, s: str) -> str:
        
        map = {}
        for i in s:
            map[i] = map.get(i,0) + 1
        
        nm = dict(sorted(map.items(), key=lambda val:val[1], reverse=True))
        
        res = ""

        for [key,val] in nm.items():
            res = res + (key)*val
        
        return res