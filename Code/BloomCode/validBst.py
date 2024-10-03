# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def util(node, min, max):
            if(node == None):
                return True
            
            if(node.val >= max or node.val <=min):
                return False
            
            left = util(node.left, min, node.val)
            right = util(node.right, node.val, max)

            return left and right
        
        res = util(root, -float(inf), float(inf))
        return res