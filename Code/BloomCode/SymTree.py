# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if(not root):
            return True
        
        def util(leftNode, rightNode):
            if(leftNode == None and rightNode == None):
                return True
            
            if(leftNode == None or rightNode == None):
                return False
            
            if(leftNode.val != rightNode.val):
                return False
            
            leftEval = util(leftNode.left, rightNode.right)
            rightEval = util(leftNode.right, rightNode.left)

            return leftEval and rightEval

        res = util(root.left, root.right)
        return res