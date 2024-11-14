"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        stk = []
        dummy = Node(0)
        cur = dummy
        stk.append(head)

        while(stk):
            tmp = stk.pop()

            if(tmp.next):
                stk.append(tmp.next)
            if(tmp.child):
                stk.append(tmp.child)
            
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None
            cur = tmp

        dummy.next.prev = None
        return dummy.next
