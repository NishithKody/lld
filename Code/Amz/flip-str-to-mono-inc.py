class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        oneCount =0 
        res = 0
        # 
        # 010110


        for val in s:
            if(val=='1'):
                oneCount += 1
            else:
                res = min(res+1, oneCount)
        
        return res
