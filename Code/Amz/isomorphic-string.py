class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chk = {}
        mapped = set()

        n = len(s)
        m = len(t)

        if(n!=m):
            return False
        
        for i in range(n):
            sVal = s[i]
            tVal = t[i]

            if(sVal not in chk):
                if(tVal in mapped):
                    return False
                chk[sVal] = tVal
                mapped.add(tVal)
            else:
                if(chk[sVal] != tVal):
                    return False

        return True
    