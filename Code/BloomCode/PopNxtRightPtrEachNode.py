"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if(root==None):
            return None

        q = deque()
        q.append(root)
        head = root

        while(len(q)>0):
            l = len(q)
            prevNode = None

            while(l>0):
                cur = q.popleft()
                if(prevNode == None):
                    cur.next = None
                    prevNode = cur
                else:
                    prevNode.next = cur
                    prevNode = cur
                
                left = cur.left
                if(left!=None):
                    q.append(left)

                right = cur.right
                if(right!=None):
                    q.append(right)
                
                l=l-1
            
        return head
