# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        - given: root node of a binary tree
        - find: max depth of tree (length of longest path)

        - use dfs and return the max depth of the current node

        - time: linear for traversing the tree
        - space: logn for the recursive call stack
        """
        # base case
        if not root:
            return 0

        # max depth of current node = 1 + max depth of children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # insert all nodes into the queue, go until it is empty
        depth = 0
        q = deque([root])
        while q:
            # process all nodes from current level
            currentNodeCount = len(q)
            for i in range(currentNodeCount):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth
            
