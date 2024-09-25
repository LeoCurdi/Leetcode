class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        """
        - given: an m * n grid, where -1 = a wall, 0 = a gate, inf = an empty space
        - return: the distance to the nearest gate, for every room

        what we know:
        - we are returning a copy of the input array, but changing the empty room values to equal their distance from the nearest gate
        - if there is no reachable gate, the value stays at inf
        - the edges of the grid can be considered walls

        intuition:
        - could run dfs on every empty position to find its nearest gate
            - this would be super inefficent (n*m)^2
        - could optimize dfs to compute the distances for all visited nodes, but it will only work for paths that end in a gate
        - could do a dfs starting at the gates instead and propagating outward.
            - for each gate:
                - do a dfs, keeping track of how far you are from the gate and updating each distance
                - if the distance has already been updated from a different gate, compare and update if closer
            - this solution is more like (n*m) * k, where k is the number of gates
                - this is still repeated work though, since were traversing the entire graph multiple times
        - best solution: use bfs from each gate, and run them simultaneously s.t. they meet in the middle
            - no repeated work
            - how to run simultaneously? start by pushing all gate indices to the queue

        - time: linear on the size of the grid, for traversing it once
        - space: linear on the size of the grid, for having potentially the entire grid in a queue 
        """
        ROWS, COLS = len(rooms), len(rooms[0]) # always a good place to start with 2d arrays
        queue = deque()
        visited = set()

        # initialize the queue with all the gates
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col)) # visit the nodes

        # bfs
        distance = 0 # starts at 0 (gate is 0 dist from itself)
        while queue:
            # go through all of the nodes that are CURRENTLY in the queue (same distance nodes)
            for i in range(len(queue)):
                cur = queue.popLeft() # get the next node
                r, c = cur[0], cur[1]
                rooms[r][c] = distance # update the distance
                # queue the next round of nodes
                queueAdjacencies(r,c)
            distance += 1 # update the distance for the next round of nodes

        # helper for queueing up adjacent rooms
        def queueAdjacencies(r, c):
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]:
                if (row in range(ROWS) and col in range(COLS) 
                and (row,col) not in visited
                and rooms[row][col] != -1):
                    queue.append((row,col))
                    visited.add((row,col)) # visit the nodes

        # we don't have to return anything, were just modifying the rooms memory


