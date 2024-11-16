class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def maxHist(h):
            res = 0
            stk = [-1]
            h.append(0)

            for i,val in enumerate(h):
                while(val<h[stk[-1]]):
                    prev_index= stk.pop()
                    prev_val = h[prev_index]
                    width = i - stk[-1] -1
                    res = max(res, width*prev_val)
                
                stk.append(i)
            
            return res
        
        ans = 0
        n = len(matrix)
        m = len(matrix[0])

        hg = [0] * m

        for i in range(n):
            for j in range(m):
                if(matrix[i][j]=='0'):
                    hg[j] = 0
                else:
                    hg[j] = hg[j] + 1
            
            print('hg',hg)
            ans = max(ans, maxHist(hg))

        return ans