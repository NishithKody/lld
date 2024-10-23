# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def find_ht(node):
            if(node is None):
                return 0
            left = find_ht(node.left)
            right = find_ht(node.right)
            return max(left,right) + 1
        
        def util(node):
            if(node is None):
                return None
            
            left_h = find_ht(node.left)
            right_h = find_ht(node.right)

            if(left_h == right_h):
                return node
            
            if(left_h > right_h):
                return util(node.left)
            else:
                return util(node.right)
        
        res = util(root)
        return res
