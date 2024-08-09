# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - given: 2 int arrays preorder and inorder of a binary tree (not BST)
        - find: an alg to construct the binary tree

        - place the root node, then use recursion to build the left and right subtrees
        """
        # base case
        if not preorder or not inorder:
            return None
        
        # we know that the first preorder element is always the root
        root = TreeNode(preorder[0])

        # get the index of the root in the inorder array
        rootIndex = inorder.index(preorder[0])

        # build the left subtree - we need to pass in all elements until the root is encountered in the inorder
        root.left = self.buildTree(preorder[1:rootIndex+1], inorder[0:rootIndex+1]) # array[a:b] includes elements a to b-1
        # build the right subtree with the rest of the elements
        root.right = self.buildTree(preorder[rootIndex+1:len(preorder)], inorder[rootIndex+1:len(inorder)])

        return root