# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# preorder and inorder list solution
# NOTE: this solution breaks when there are multiple same value nodes, see alt solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """
        - construct lists for the preorder and inorder traversal and return them joined into a string
        """
        if not root:
            return ""
        self.preorder, self.inorder = [], []

        def helper(cur):
            if not cur:
                return
            # enter value into the preorder table
            self.preorder.append(str(cur.val))
            helper(cur.left)
            #enter val into the in order table
            self.inorder.append(str(cur.val))
            helper(cur.right)

            return
        
        helper(root)
        # return a string containing the comma separated preorder values followed by the inorder
        preorderString = ",".join(self.preorder)
        inorderString = ",".join(self.inorder)
        result = preorderString + "." + inorderString
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        """
        - parse the preorder/inorder string into lists and use a tree building alg to build the tree from the 2 lists
        """
        if len(data) == 0:
            return None
        
        # parse the string into preorder and inorder arrays
        parts = data.split(".")
        preorderList = parts[0].split(",")
        inorderList = parts[1].split(",")

        # use alg to build a tree from preorder and inorder arrays
        def buildTree(preorder, inorder):
            # base case
            if not preorder or not inorder:
                return None
            
            # we know that the first preorder element is always the root
            root = TreeNode(int(preorder[0]))

            # get the index of the root in the inorder array
            rootIndex = inorder.index(preorder[0])

            # build the left subtree - we need to pass in all elements until the root is encountered in the inorder
            root.left = self.buildTree(preorder[1:rootIndex+1], inorder[0:rootIndex+1]) # array[a:b] includes elements a to b-1
            # build the right subtree with the rest of the elements
            root.right = self.buildTree(preorder[rootIndex+1:len(preorder)], inorder[rootIndex+1:len(inorder)])

            return root
        
        return buildTree(preorderList, inorderList)
        
# dfs preorder solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """
        - records the preorder traversal of the tree including null children
        """
        # global var
        self.preorderList = []

        # dfs helper
        def helper(cur):
            # base case
            if not cur:
                self.preorderList.append("NULL")
                return
            
            # visit nodes in preorder
            self.preorderList.append(str(cur.val))
            helper(cur.left)
            helper(cur.right)

        # return the list as a comma separated string
        helper(root)
        return ",".join(self.preorderList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        - uses the preorder list to construct the tree
        """
        # global variables
        preorderList = data.split(",")
        self.i = 0

        # dfs helper
        def helper():
            # base case
            if preorderList[self.i] == "NULL":
                self.i += 1
                return None
            
            # create the current node
            cur = TreeNode(int(preorderList[self.i]))
            self.i += 1

            # recursively build the left and right subtrees
            cur.left = helper()
            cur.right = helper()

            # return the current node
            return cur

        return helper()