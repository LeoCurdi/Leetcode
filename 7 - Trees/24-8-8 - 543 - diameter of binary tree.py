# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        - given: root of binary tree
        - find: the diameter of the tree (the length of the longest path between any 2 nodes)

        - use dfs. at each node, check the longest path that goes through it, thus checking all possible longest paths
        """
        result = 0

        def helper(root):
            # give helper access to result
            nonlocal result

            #base case
            if not root:
                return 0

            # compute the max path through root
            depthLeft = helper(root.left) 
            depthRight = helper(root.right)
            curMax = depthLeft + depthRight
            result = max(result, curMax)

            # return the depth of the tree
            return 1 + max(depthLeft, depthRight)

        helper(root)
        return result

            