class Solution:
    def validTree(self, n, edges):
        """
        - given: n nodes labled 0 to n-1, a list of undirected edges
        - return: whether the edges make a valid tree

        what we know:
        - undirected edges go both ways
        - to be a valid tree, it has to have the traditional tree structure
            - trees cannot have loops, in other words sibling nodes cant connect to each other
            - also, a tree must be connected, so it cant have multiple components
            - a node can have as many children as it wants and still be valid

        intuition:
        - we need a data structure to rep. the graph so that we can traverse it easily
            - use a hashmap to map a node to its adjacent nodes
        - now that we can traverse the graph, we just need to check for cycles and multiple components
            - use dfs for traversal
        - how to check for cycles?
            - standard cycle detection: visit nodes and check if a node is being visited more than once
        - how to check for multiple components?
            - after visiting an entire component, check if the number of visited nodes equals the number of input nodes
        - how to know what node to start the dfs from, so that we can visit the whole graph in one dfs call?
            - were assuming that 0 is the root of the tree
        
        - time: linear (n + e) since we traverse the whole graph once
        - space: linear (n) for the depth of the call stack and for the visited list
        """
        graphHashMap = {i:[] for i in range(n)} # initialize the hash map
        visitedNodes = set()

        # insert all edges into the hashmap
        for a, b in edges:
            graphHashMap[a].append(b)
            graphHashMap[b].append(a) # edges go both ways

        def dfsHelper(n, prev): # use the prev parameter to avoid going back to the parent
            # base case: loop detected
            if n in visitedNodes:
                return False
            
            # remove parent from adjacencies list
            adjacentNodes = graphHashMap[n]
            adjacentNodes.pop(prev)

            # branch to adjacencies. NOTE: if there are no adjacencies it will automatically skip to the return
            visitedNodes.add(n)
            for m in adjacentNodes:
                if not dfsHelper(m, n):
                    return False
                
            return True

        if dfsHelper(0, -1):
            if len(visitedNodes) == n: # check for not connected graph
                return True
            
        return False



