# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []
        count = 0
        temp = head

        while(temp!=None):
            temp = temp.next
            count += 1
        
        # print('count',count)
        temp = head

        for i in range((count//2)-1):
            temp = temp.next
        
        if(count%2==1):
            temp = temp.next
        
        prev= None
        cur=temp
        nxt=temp

        while(cur!=None):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        temp = head
        for i in range(count//2):
            if(temp.val!=prev.val):
                return False
            
            temp=temp.next
            prev=prev.next
        
        return True
       