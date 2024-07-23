# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def util(ind, pre):
            if(len(ind)==0 or len(pre)==0):
                return None
            
            val = ind[0]
            root = TreeNode(val)
            if(val not in pre):
                return None

            ind.pop(0)
            index = pre.index(val)
            root.left = util(ind,pre[:index])
            root.right = util(ind,pre[index:])

            return root
        
        res = util(preorder, inorder)

        return res

        