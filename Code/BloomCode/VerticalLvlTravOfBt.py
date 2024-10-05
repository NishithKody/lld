# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        map = defaultdict(list)
        q = deque()
        q.append([root,0,0])

        while(len(q)>0):
            cur = q.popleft()
            [node,dist,level] = cur
            
            map[dist].append((level,node.val))

            left = node.left
            if(left != None):
                q.append([left, dist-1, level+1])
            
            right = node.right
            if(right != None):
                q.append([right, dist+1, level+1])

        
        for key in sorted(map.keys()):
            row = sorted(map[key], key=lambda item:(item[0],item[1]))
            tmp = []
            for [l,n] in row:
                tmp.append(n)
            res.append(tmp)

        return res
        