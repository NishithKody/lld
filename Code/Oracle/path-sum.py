# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def util(node, val):
            if node is None:
                return False
            
            cur = val + node.val
            if(cur == targetSum and node.left == None and node.right == None):
                return True
            
            left = util(node.left, cur)
            right = util(node.right, cur)

            return left or right
        
        return util(root, 0)
