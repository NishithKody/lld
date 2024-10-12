# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        lst2 = []
        carry = 0

        res = ListNode()
        head = res

        while(l1!=None):
            val = l1.val
            lst1.append(val)
            l1=l1.next
        
        while(l2!=None):
            val = l2.val
            lst2.append(val)
            l2=l2.next

        while(len(lst1)>0 or len(lst2)>0 or carry==1):
            val1 = lst1.pop() if len(lst1)>0 else 0
            val2 = lst2.pop() if len(lst2)>0 else 0
            addVal = val1 + val2 + carry

            tmp = addVal % 10
            carry = addVal // 10

            newNode = ListNode(tmp,res.next)
            res.next = newNode

        return res.next
