
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stk = [-1]
        res = 0
        h.append(0)

        for i,val in enumerate(h):
            while(val< h[stk[-1]]):
                pop_index = stk.pop()
                prev_val = h[pop_index]
                width = i - stk[-1] -1
                res = max(res, width * prev_val)

            stk.append(i)

        return res

        