# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - given: the root of a binary tree
        - find: the level order (left to right and top to bottom) of the nodes' values, grouped by level in a 2d array
        
        - use standard BFS alg. hit each node in level i before moving to the next level
        """
        # edge case
        if not root:
            return []

        result = []

        # use a queue
        q = deque([root])

        # until there are no nodes left
        while q:
            # process all of the prev level and insert all of the next level
            curValues = []
            nodeCount = len(q)
            for i in range(nodeCount):
                node = q.popleft()
                curValues.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(curValues)

        return result