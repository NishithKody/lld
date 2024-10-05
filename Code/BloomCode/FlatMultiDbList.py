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
        
        def util(node, val):

            if(node == None):
                return val

            pt = node
            
            while(pt!=None):
                tmp = []
                val.append(pt.val)
                if(pt.child!=None):
                    tmp = util(pt.child,[]) 
                    for i in tmp:
                        val.append(i)
                pt = pt.next
            
            return val
        
        res = util(head,[])
        return res