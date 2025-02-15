# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if(not root):
            return []
            
        res = []
        q = deque()

        flip = False

        q.append(root)

        while(q):
            l = len(q)
            level = []

            for _ in range(l):
                cur = q.popleft()
                level.append(cur.val)

                if(cur.left):
                    q.append(cur.left)
                
                if(cur.right):
                    q.append(cur.right)
            
            if(flip):
                res.append(level[::-1])
            else:
                res.append(level)
            flip = not flip
        return res
    