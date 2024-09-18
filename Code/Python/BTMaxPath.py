# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0

        res = [root.val]

        def util(node):
            if(node==None):
                return 0
            
            leftMax = max(util(node.left),0)
            rightMax = max(util(node.right),0)

            curMax = node.val + leftMax +rightMax
            if(curMax > res[0]):
                res[0] = curMax
            
            return node.val + max(leftMax, rightMax)
        
        util(root)
        return res[0]
        