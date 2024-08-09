# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        - given: a BST
        - find: whether it is valid (in sorted order)

        - use dfs in order traversal, which traverses the tree in sorted order.
          you just have to check if the prev node is less than the next node

        - time: linear for visiting each node once
        - space: logarithmic for the recursive call stack
        """
        # global result and prev node variable
        self.result = True
        self.prevNodeVal = float("-infinity")

        # dfs helper
        def helper(root):
            # base case
            if not root:
                return
            
            # traverse the tree and visit in order
            helper(root.left)
            if root.val < self.prevNodeVal: # this is the validating condition
                self.result = False
            self.prevNodeVal = root.val
            helper(root.right)
            
            return
        
        helper(root)
        return self.result