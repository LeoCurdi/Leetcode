
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        - given: a node in a connected undirected graph
        - return: a deep copy of the graph

        what we know:
        - the graph is undirected, so we can traverse edges in any direction
        - since the graph is connected, it's easy to traverse the whole thing
        - for edges, each node has a list of pointers to adjacent nodes
        - the node's value is the same as its index
        - we're given the first node (val = 1)
        - we must return a ref. to the corresponding node in the copy

        intuition:
        - could use dfs or bfs to traverse the graph
        - we're running into issues where we could encounter the same node twice, or its hard to update when there's multiple edges to the same node (node 4 in the example)
            - we can solve this with a hash map:
                - traverse the graph
                - create a clone of each node
                - use the hashmap to map the old nodes to their copy
            - the hashmap allows to check for duplicates in constant time
            - additionally, we can use the node references in the hashmap to create the new connections
        - the dfs calls can return a ref to the current node so that the parent call can create a connection to it
            
        - time: linear time on the size of the graph (N + E)
        - space: linear, since we're storing the entire graph in a hash map
        """
        oldToNewMap = {} # key: old nodes, value: new nodes

        def dfsHelper(cur):
            # base case: we already cloned the node
            if cur in oldToNewMap:
                return oldToNewMap[cur] # return a ref to the new node
            
            # create the node clone
            copy = Node(cur.val)
            oldToNewMap[cur] = copy

            # branch to the adjacent nodes
            for neighborNode in cur.neighbors:
                ref = dfsHelper(neighborNode)
                copy.neighbors.append(ref)

            # return a ref to the copy
            return copy
        
        return dfsHelper(node) if node else None # return the head ref of the new graph
