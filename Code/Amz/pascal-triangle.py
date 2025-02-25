class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        res.append([1])
        if(numRows==1):
            return res
        
        res.append([1,1])
        if(numRows==2):
            return res

        for i in range(3,numRows+1):
            prevRow = res[-1]
            cur = [1]*i
            for j in range(1,i-1):
                cur[j] = prevRow[j-1] + prevRow[j]
            
            res.append(cur)
        
        return res
    