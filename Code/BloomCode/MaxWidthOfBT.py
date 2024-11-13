# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        res = 0
        q.append((root,1))

        while(len(q)>0):
            first_node = q[0][1]
            last_node = q[-1][1]
            val = last_node - first_node + 1
            res = max(res, val)

            for _ in range(len(q)):
                cur, index = q.popleft()

                index = index - 1 # this is optimization

                if(cur.left):
                    q.append((cur.left, index*2 ))
                
                if(cur.right):
                    q.append((cur.right, (index*2) +1 ))
        
        return res