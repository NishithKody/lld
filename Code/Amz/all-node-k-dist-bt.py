# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        visit = set()

        def util(node,prt):
            if(node is None):
                return
            
            parent[node] = prt
            
            util(node.left, node)
            util(node.right, node)
        
        util(root,None)

        res = []

        q = deque()
        q.append(target)
        count = 0
        visit.add(target)

        while(q):
            l = len(q)
            if(count==k):
                break
            
            for _ in range(l):
                cur = q.popleft()

                if(cur.left and cur.left not in visit):
                    visit.add(cur.left)
                    q.append(cur.left)
                
                if(cur.right and cur.right not in visit):
                    visit.add(cur.right)
                    q.append(cur.right)
                
                if(parent[cur] and parent[cur] not in visit):
                    visit.add(parent[cur])
                    q.append(parent[cur])
            count += 1

        for node in q:
            res.append(node.val)
        return res


