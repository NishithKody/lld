# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        q = deque()
        q.append((root,1))

        while(len(q)>0):
            curLen = 0
            firstInd = q[0][1]
            lastInd = q[-1][1]
            curLen = lastInd - firstInd + 1
            res = max(res, curLen)

            for _ in range(len(q)):
                cur, val = q.popleft()

                if(cur.left):
                    q.append((cur.left, val*2))
                
                if(cur.right):
                    q.append((cur.right, val*2+1))
        
        return res
                