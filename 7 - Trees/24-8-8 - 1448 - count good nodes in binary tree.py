# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        - given: root of tree
        - find: the number of good nodes in the tree. a node is good if the path to it from the root doesn't contain any greater nodes
        
        - use DFS and keep track of the current max of the path
        """
        # use a global result varaible
        self.result = 0

        # use a helper function so we can keep track of path max
        def helper(root, curMax):
            # base case
            if not root:
                return
            # check if current node is a max, and update path max
            if root.val >= curMax:
                self.result += 1
                curMax = root.val
            # run the alg on the children
            helper(root.left, curMax)
            helper(root.right, curMax)

        helper(root, root.val)
        return result