# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        - given: a binary tree
        - find: the path with the highest sum (a path cannot go through the same node twice)
       
        - for a path to be valid, it can only have one split (where the path goes through both children of a node, this node must be the highest point of the path)
        - compute the left and right subproblems using recursion
            -  for each node (starting from the leaves):
                - compute and save the max path, then compute and return the max path without splitting
                - the max path for a node is: the max paths of the left and right subtrees + the current node value
        
        - time: linear for visiting each node once
        """
        # edge case
        if not root:
            return 0

        # global vars
        self.result = float("-inf")

        def helper(cur):
            # base case
            if not cur:
                return 0

            # first calculate the subproblems
            maxLeftPathNoSplit = helper(cur.left)
            maxRightPathNoSplit = helper(cur.right)

            # discount negative paths, as we wont include them if we dont have to
            if maxLeftPathNoSplit < 0:
                maxLeftPathNoSplit = 0
            if maxRightPathNoSplit < 0:
                maxRightPathNoSplit = 0

            # calculate the max path for this node
            curMaxPath = cur.val + maxLeftPathNoSplit + maxRightPathNoSplit
            self.result = max(self.result, curMaxPath)

            # return the max non splitting path through the current node
            return cur.val + max(maxLeftPathNoSplit, maxRightPathNoSplit)
        
        helper(root)
        return self.result
            
