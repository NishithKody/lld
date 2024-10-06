class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ct1 = [0] * 26
        ct2 = [0] * 26
        n = len(s)
        count = 0

        if(len(s)!=len(t)):
            return -1

        for i in s:
            val = ord(i) - ord('a')
            ct1[val] = ct1[val] + 1
        
        for i in t:
            val = ord(i) - ord('a')
            ct2[val] = ct2[val] + 1

        for i in range(26):
            val = abs(ct1[i]-ct2[i])
            count = count + val

        return count//2
