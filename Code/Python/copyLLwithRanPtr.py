"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        map  = {}
        res = Node(0)
        temp = head
        resHead = res

        while(temp!=None):
            nd = Node(temp.val)
            res.next = nd
            map[temp] = nd
            res=res.next
            temp = temp.next
        
        temp = head
        res = resHead.next

        while(temp!=None):
            ranNode = temp.random
            nrn = None
            if(ranNode != None):
                nrn = map[ranNode]

            res.random = nrn
            temp = temp.next
            res=res.next

        
        return resHead.next

        