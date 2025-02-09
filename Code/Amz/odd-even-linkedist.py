# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None:
            return None
        evenHead = ListNode(0)
        tmp = evenHead
        count = 1
        res = head
        prev =head
        while(head!=None):
            if(count%2==1):
                prev = head
                head = head.next
            else:
                nxt = head.next
                prev.next = nxt
                head.next = None
                evenHead.next = head
                evenHead = evenHead.next

                head = nxt
            count +=1
        
        prev.next = tmp.next
        return res
