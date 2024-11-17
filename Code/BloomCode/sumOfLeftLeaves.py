# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def util(node, prev):
            if(node==None):
                return
            
            if(prev == 'L'):
                if(node.left == None and node.right==None):
                    res[0] += node.val
            
            util(node.left, 'L')
            util(node.right,'R')

        
        util(root,"S")
        return res[0]