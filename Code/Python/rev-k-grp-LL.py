# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev(node):
            prev = None
            cur = node
            while(cur!=None):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
        
        dummy = ListNode(0,head)
        prev_group = dummy

        while(head!=None):
            current = head
            count = 0

            while(count<k and current!=None):
                current = current.next
                count += 1
            
            if(count == k):
                # 1 <- 2 <- 3  4-> 5
                grp_end = head
                for _ in range(k-1):
                    grp_end = grp_end.next
                
                next_grp = grp_end.next
                grp_end.next = None
                new_head = rev(head)

                prev_group.next = new_head
                head.next = next_grp

                prev_group = head
                head = next_grp

            else:
                # print('no valid count')
                break

        return dummy.next
