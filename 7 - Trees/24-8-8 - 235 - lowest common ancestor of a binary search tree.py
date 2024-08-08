# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - given: a BST
        - find: the lowest common ancestor node of 2 given nodes in the tree (a node can be an ancestor of itself)

        - it's a BST, so ancestors must be between the values of p and q
        - since a node in a BST is basically a pivot between lower and higher values, 
          any node valued between p and q must be the LCA,
          as the lower of the 2 must be in the left subtree and the higher must be in the right
        
        - time: height of tree = logn
        - space: constant since were not using any extra data structures
        """
        # make p the lower node for consistency
        if p.val > q.val:
            p, q = q, p

        # iterate to the LCA
        cur = root
        while cur.val < p.val or cur.val > q.val:
            if cur.val < p.val:
                cur = cur.right
            if cur.val > q.val:
                cur = cur.left
        
        # now cur is between p and q, inclusively
        # either cur = p and q is to the right, or cur = q and p is to the left, or p < cur < q and theyre on opposite sides,
        # so this must be the pivot
        return cur

        