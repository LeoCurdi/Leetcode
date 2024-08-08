# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        - given: the roots of 2 binary trees
        - find: whether subroot is a subtree of root

        - dfs through the main tree, checking if each node is the same tree as the subtree
        - use isSameTree() function from prev leetcode
        """
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # base case - one or both of roots is null
            if not p and not q:
                return True
            if not p or not q:
                return False

            # if left and right subtrees are the same, and current nodes are the same
            if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                return True
            else:
                return False
            
        #base case
        if not root:
            return not subRoot

        # this node contains a subtree if: the left node contains a subtree, or the right node contains a subtree, or this node is a subtree
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


