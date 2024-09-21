
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]

        def util(node):
            if(node==None):
                return 0
            
            left = util(node.left)+1
            right = util(node.right) +1

            if(left>right):
                val = left - right
                if(val>=2):
                    res[0] = False
            else:
                val = right - left
                if(val>=2):
                    res[0] = False
            
            return max(left,right)

        util(root)
        return res[0]