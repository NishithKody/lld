# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk  = []
        res = 0

        slw = fst = head

        while(slw!=None and fst!=None):
            stk.append(slw.val)
            slw = slw.next
            fst = fst.next
            
            if(fst!=None):
                fst=fst.next
        
        # print('stk',stk)
        # print('slw',slw)

        while(slw!=None):
            curVal = slw.val
            stkVal = stk.pop()
            # print('cur,stkval',curVal,stkVal)
            curSum = curVal + stkVal
            res = max(res, curSum)
            slw = slw.next
        
        return res

        
