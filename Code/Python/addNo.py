# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0

        while(l1 or l2 or carry==1):
            v1 = l1.val if(l1!=None) else 0
            v2 = l2.val if(l2!=None) else 0

            val = v1 + v2 + carry
            carry = val//10
            val = val % 10

            nn = ListNode(val)
            res.next = nn
            res = res.next
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        
        return head.next


            

