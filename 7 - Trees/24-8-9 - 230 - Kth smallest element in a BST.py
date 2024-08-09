# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        - given: root of BST, an integer k
        - find: the kth smallest element in the tree

        - uses in order dfs and counts how many elements have been visited

        - time: linear for visiting the entire tree
        - space: logarithmic for the dfs call stack
        """
        self.currentPos = 0
        self.result = 0

        # helper returns true when the target is found, so we dont have to do additional searching
        def helper(cur):
            if not cur:
                return False
            
            if helper(cur.left):
                return True
            self.currentPos += 1
            if self.currentPos == k:
                self.result = cur.val
                return True
            return helper(cur.right)
        
        helper(root)
        return self.result
    
    # iterative solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        stack = []
        cur = root
        count = 0

        # go until the stack is empty or were out of tree
        while cur or stack:
            # traverse left first
            while cur:
                stack.append(cur)
                cur = cur.left
            # visit the current node
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            # traverse right
            cur = cur.right
            
        
