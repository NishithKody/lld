class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n

        stk = []
        iStk = []
        stk.append(temp[n-1])
        iStk.append(n-1)

        for i in range(n-2, 0-1,-1):
            cur = temp[i]

            while(len(stk)>0 and cur>=stk[len(stk)-1]):

                stk.pop()
                iStk.pop()
            if(len(stk)==0):
                res[i] = 0
            else:
                res[i] = iStk[len(iStk)-1] - i

            stk.append(cur)
            iStk.append(i)
        
        return res
        