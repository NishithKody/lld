"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        res = []
        def dfs(node):
            if(node == None):
                return 
            
            left = dfs(node.left)
            res.append(node)
            right = dfs(node.right)
        
        dfs(root)

        for i,node in enumerate(res):
            if(node == p and i+1<len(res)):
                 return res[i+1]
        
        return None
