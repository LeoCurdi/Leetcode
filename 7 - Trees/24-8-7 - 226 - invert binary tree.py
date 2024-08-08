# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        - given: root of binary tree
        - find: alg to invert the tree

        - all you have to do is swap the children nodes
        - iterate using dfs
        """
        # base case
        if not root:
            return None
        
        # swap children
        root.left, root.right = root.right, root.left

        # dfs
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root