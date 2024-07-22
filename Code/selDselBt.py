# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if(root == None):
            return 'None'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(',')

        def util():
            if(len(nodes)==0):
                return
            
            if(nodes[0]=='None'):
                nodes.pop(0)
                return None

            val = nodes[0]
            nodes.pop(0)
            root = TreeNode(val)
            root.left = util()
            root.right = util()

            return root
        
        res = util()
        return res
        
