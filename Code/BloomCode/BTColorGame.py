# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        def find_node(node):
            if(node == None):
                return None
            
            if(node.val == x):
                return node
            
            left = find_node(node.left)
            right = find_node(node.right)
            
            return left or right
        
        def count_nodes(node):
            if(node == None):
                return 0
            
            left = count_nodes(node.left) 
            right = count_nodes(node.right) 

            return left + right + 1
        
        reqNode = find_node(root)
        leftCount = count_nodes(reqNode.left)
        rightCount = count_nodes(reqNode.right)

        res = max(leftCount, rightCount, n-rightCount-leftCount-1)
        return res>n//2