class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        - given: an int n, an array of edges
        - return: the number of connected components in the graph

        what we know:
        - edges i = [a, b], where a and b are connected in both directions
        - we have n nodes, that are labeled as 0 to n-1

        intuition:
        - since the edges go both ways, we can start at any node and find its entire component
        - all we need to do is call a traversal alg on one node in each component and return how many calls were made
            - lets do dfs
        - how not to search (and count) the same component twice?
            - mark all nodes as visited when traversing them
        - how to efficiently sift through the edges to traverse in linear time?
            - insert all edges into a hashmap (constant time access)
        - how to protect the traversal against loops?
            - dont traverse to nodes that have already been visited
        - edge case: how to avoid going back and forth between the same 2 nodes?
            - well need to pass the prev node to dfs to avoid it

        - time: linear on nodes + edges, since were visiting the entire graph once
        - space: linear on nodes + edges, for inserting all data into a hashmap
        """
        edgeMap = {i:[] for i in range(n)} # initialize the hashmap
        visitedNodes = set()

        # fill the map
        for a, b in edges:
            # edges go both ways so we must map the edge to both nodes
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        # define a helper for traversal (dfs is good)
        def dfsHelper(cur, prev):
            # remove prev from the adjacencies list to smooth out the code
            adjs = edgeMap[cur]
            if prev in adjs:
                adjs.remove(prev)

            # base case: cur has been visited
            if cur in visitedNodes:
                return

            # visit the current node
            visitedNodes.add(cur)

            # traverse to each neighbor
            # base case is baked into this (if there are no neighbors it just returns)
            for adj in adjs:
                dfsHelper(adj, cur)

        res = 0
        for i in range(n):
            if i not in visitedNodes:
                dfsHelper(i, -1) # -1 is a good burner prev since its not a possible node
                res += 1 # count the component

        return res
    
    
    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        """
        - neetcode solution using union find
            - says this problem was literally made for union find
        - too hard to explain, watch the video
        - uses the idea of path compression

        - time: linear on number of edges?
        """
        parents = [i for i in range(n)] # a mapping of nodes (indexes) to their root parent node (the value)
        nodeRanks = [1] * n # the ranking of each node (indexes). all default to 1 at first

        # helper to find the root parent of a node
        def findRootParent(n1):
            res = n1
            while res != parents[res]:
                parents[res] = parents[parents[res]] # path comression (remove linked lists)
                res = parents[res] # find the root

            return res
        
        def unionFind(n1, n2):
            # get the root parents
            p1, p2 = findRootParent(n1), findRootParent(n2)

            # if they have the same root parent
            if p1 == p2: 
                return 0 # indicate that we did not perform a union
            
            # otherwise perform the union
            if nodeRanks[p2] > nodeRanks[p1]: # using ranks allows for making an efficient union thats more like a tree rather than a linked list
                parents[p1] = p2
                nodeRanks[p2] += nodeRanks[p1]
            else: 
                parents[p2] = p1
                nodeRanks[p1] += nodeRanks[p2]

            return 1 # count the union operation
        
        res = n # result starts with n separate components, and subtracts one each time a node is unioned to another
        # try to union each node
        for n1, n2 in edges:
            res -= unionFind(n1, n2)

        return res