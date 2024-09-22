class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        - given: an m*n array of binary nums (1 rep. land, 0 rep. water)
        - find: the area of the largest island

        what we know:
        - an island has to be completely surrounded by water
        - if 2 1's are diagonal to each other, they don't count as connected
        - the edges of the grid are all considered water

        intuition:
        - this is just like the count number of islands problem, but modified to track the total area
        - model the grid as a graph, where nodes are connected if they're adjacent to each other
        - call dfs on each node in the graph
            - if its a 1, continue to each of the adjacencies
            - each time a 1 is encountered, add one to the sum of the current island
        - compare against the result to see if there's a new result
        - how to avoid duplicate counting? use a set to track each node that's been visited

        - time: n*m, for visiting each node once
        - space: n*m for the max depth of the call stack
        """
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        visitedNodes = set()

        def dfsHelper(row, col):
            # case - out of bounds
            if row not in range(ROWS) or col not in range(COLS):
                return 0

            # case - not land or visited
            if grid[row][col] == 0 or (row,col) in visitedNodes:
                return 0

            # case - valid land
            curArea = 1 # add to area count
            visitedNodes.add((row,col)) # mark as visited
            for row, col in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]: # check adjacencies
                curArea += dfsHelper(row, col) # accumulate the area of the rest of the search
            return curArea

        # call dfs on each node in the grid
        for row in range(ROWS):
            for col in range(COLS):
                # if its not land, you can just skip it
                if grid[row][col] != 0 and (row,col) not in visitedNodes:
                    result = max(result, dfsHelper(row, col))

        return result