# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        - given: root of a binary tree
        - find: whether it is height-balanced (each node's children differ in height by at most 1)
        
        - use dfs and check if each node is balanced
        """
        # create a member variable so the helper has access
        self.result = True

        # we need a recursive helper function, since it needs to return the depth of each node rather than true/false
        def dfs(cur):
            # base case
            if not cur:
                return 0
            
            # check if the current node is balanced (depths of children must not differ by more than 1)
            leftH = dfs(cur.left)
            rightH = dfs(cur.right)
            if leftH < rightH-1 or rightH < leftH-1:
                self.result = False
            
            # return the depth
            return 1 + max(leftH, rightH)

        dfs(root)
        return self.result