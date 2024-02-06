# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        - The tree is still the same top to bottom, we just need to mirror it
          such that the left side and right side reverse.
        - All we have to do is swap all children (we will use a DFS recursion).
        """
        # base case: null node
        if not root:
            return None # None means null
    
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # perform invertTree() on left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the root of the inverted tree
        return root
