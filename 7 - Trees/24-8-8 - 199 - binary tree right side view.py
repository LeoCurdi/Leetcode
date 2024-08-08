# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        - given: root of tree
        - find: a list of all the rightmost nodes of each level

        - use standard BFS, and save the last node from each level
        """
        if not root:
            return []

        result = []
        q = deque([root])
        while q:
            count = len(q)
            rightNode = None
            for i in range(count):
                # pop a node
                node = q.popleft()
                # save the right node
                if i == count - 1:
                    rightNode = node
                # push children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(rightNode.val)
        
        return result