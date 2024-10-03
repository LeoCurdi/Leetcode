class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        - given: a graph that was originally a tree but has one edge added
        - return: an edge that can be removed s.t. the graph becomes a tree again

        what we know:
        - there are n nodes labeled from 1-n
        - n = len(edges)
        - edges[i] = [a,b] indicates that a and b are adjacent
        - a tree cannot have a cycle
        - the edges in a tree go both ways
        - there may be multiple possible answers
            - in example 1, you could remove any one of the edges and it would still be a tree
        - the problem doesn't specify if the tree is binary
            
        intuition:
        - the extra edge is creating a cycle
            - if there is no cycle, then the tree can be considered valid (you can redraw it to look like a tree)
        - when there is a cycle, any one of the edges involved can be removed to break the cycle, but keep the tree structure intact
            - the only edges that arent valid candidates for removal are those that lead to an eventual leaf node (it would be cut off)
        - so find the cycle, then remove any one edge from it
            - use dfs to search the tree
            - when a cycle is detected, simply remove the previous edge
                - keep track of prev node
            - how to detect cycle?
                - mark nodes as visited
            - how to avoid going backwards and creating an inf loop between adjacent verts?
                - pass in the prev node as a parameter
            - how to construct the graph?
                - map each node to its neighbors with a hashmap (constant time access)
                - nodes are from 1-n, where n = len(edges)
            
        - time: linear on n+e = 2n = n, since we traverse the entire graph once
        - space: linear for inserting all connections into a hashmap
        
        - CURVEBALL: if multiple solutions exist, we have to return the one that comes last in the edges array
            - this solution doesn't work for this reason. we could implement n^2 checking to make it return the correct edge, 
              but the efficient solution uses union find
        """
        neighborMap = {i:[] for i in range(1, len(edges) + 1)} # init the map
        edge = [-1,-1]
        visitedNodes = set()

        # fill the map
        for a, b in edges:
            neighborMap[a].append(b)
            neighborMap[b].append(a) # connections go both ways

        # dfs traversal
        def dfsHelper(cur, prev):
            # remove prev from neighbors list
            neighbors = neighborMap[cur]
            if prev in neighbors: 
                neighbors.remove(prev)

            # cycle detected
            if cur in visitedNodes:
                # remove the prev edge
                edge[0], edge[1] = prev, cur
                return

            # hit a leaf node
            if len(neighbors) == 0:
                return

            # call for each neighbor
            visitedNodes.add(cur)
            for node in neighbors:
                dfsHelper(node, cur)

        # call dfs on the first node (could probably call it on any one node)
        dfsHelper(1, -1) # dummy value for prev

        return edge


    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        """
        - use union find
            - utilizes the fact that if there is a cycle in a graph, then there is multiple paths from node a to b in the cycle
                - aka a redundant connection
            - we just need to find what edge creates the redunancy
        - keep a parents map 
            - use an array where indices are nodes
        - keep a rank map to determine which node becomes the child and which becomes the parent
        - iterate through every edge
        - update parents and rank of node a or b in the edge
        - once we find an edge that forces us to merge a and b but a and b share a parent, that edge is redundan
        """
        parents = [i for i in range(len(edges) + 1)] # dont use the first element (no node 0)
        ranks = [1] * (len(edges) + 1) # init all ranks to 1

        def findRootParent(cur):
            p = parents[cur]
            # get the root parent
            while p != parents[p]:
                parents[p] = parents[parents[p]] # path compression: shorten the lengths from child to root parent to make the alg more efficient
                p = parents[p]

            # return the root parent
            return p
        
        def union(a, b):
            # to union them, we need to find both their root parents first
            pA, pB = findRootParent(a), findRootParent(b)

            # if both parents are equal, then completing this union would add a redundant edge
            if pA == pB:
                return False
            
            # union them by rank
            if ranks[pA] > ranks[pB]:
                parents[pB] = pA # a will be parent
                ranks[pA] += ranks[pB]
            else:
                parents[pA] = pB # b will be parent
                ranks[pB] += ranks[pA]
            return True
        
        edge = [-1,-1]
        # all we have to do is union each 2 nodes that are adjacent, until we find a redundant edge
        for a, b in edges:
            if not union(a,b):
                edge = [a,b]
        
        # return the last redundant edge that we find
        return edge
                 
