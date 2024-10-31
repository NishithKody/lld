class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        val = list(num)
        cnt = 0
        for s in val:
            while(stk and s<stk[-1] and cnt<k):
                prev_val = stk.pop()
                cnt += 1

            stk.append(s)
        
        while(stk and cnt<k):
            stk.pop()
            cnt += 1

        res_str = ''.join(stk)
        rem_zero = res_str.lstrip('0')
        return rem_zero if len(rem_zero)>0 else '0'
    