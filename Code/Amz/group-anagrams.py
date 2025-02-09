class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapAnagram = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for ch in st:
                val = ord(ch)-ord('a')
                count[val] += 1
            
            mapAnagram[tuple(count)].append(st)
        
        res = []

        for [k,v] in mapAnagram.items():
            res.append(v)
        
        return res

