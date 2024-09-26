class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - given: an m*n grid, where 0 = empty cell, 1 = fresh orange, 2 = rotten orange,
                 every 1 minute, all fresh oranges that are adjacent to the rotten orange becomes rotten
        - return: the time until all oranges are rotten

        what we know:
        - oranges have to be touching (4-way adjacent) for the rot to spread, so if an orange is not connected to a rotten orange, it can never rot
        - the grid can start with any amount of rotten oranges
        
        intuition:
        - we can model the grid as a graph, where adjacent cells are connected with an edge
        - for graphs we have 2 algs: dfs and bfs
        - we want bfs for this problem, since were trying to count the amount of iterations until we cover the whole graph
        - what if there are multiple rotten oranges to start?
            - run bfs from all of them at the same time, let them meet in the middle
            - do this with a queue, and start by queueing up all the initially rotten oranges
            - once they've finished (empty queue), return the total number of rounds of bfs
        - what if the answer is infinity?
            - before returning, do a final scan to check for clean oranges

        - time: linear (n*m), since were traversing the entire grid once
        - space: linear, since we could potentially have the entire grid inside the queue
        """
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshCount = 0

        # start by pushing all rotten oranges to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshCount += 1 # use the total amount of fresh oranges to get out of edge cases
        
        # edge case
        if freshCount == 0:
            return 0

        # helper function to check the conditions for queueing adjacent nodes
        def queueAdjacencies(node):
            r, c = node
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]: # for all 4 adjacencies
                if (row in range(ROWS) and col in range(COLS)
                    and grid[row][col] == 1):
                    queue.append((row,col))
                    grid[row][col] = 2 # basically marking the node as visited

        time = 0
        # run bfs
        while queue:
            # each round of bfs, we want to process all nodes from the prev round
            for i in range(len(queue)):
                node = queue.popleft() # pop the cell
                queueAdjacencies(node) # push all adjacent cells (if they meet the conditions)
                
            time += 1 # increment time

        # check for unreachable oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time - 1