# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - given: the roots of 2 binary trees
        - find: whether they are the same
        """
        # base case - one or both of roots is null
        if not p and not q:
            return True
        if not p or not q:
            return False

        # if left and right subtrees are the same, and current nodes are the same
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True