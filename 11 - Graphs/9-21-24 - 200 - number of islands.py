class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - given: an m*n array of binary nums, 1 represents land, 0 represents water
        - find: the number of islands
        
        what we know
        - an island has to be completely surrounded by water
        - lands that are diagonal to each other are not considered connected
        - edges of the grid count as water

        intuition
        - pick an index in the grid to start (say 0,0)
        - call a recursive search function (dfs) on that index
            - if its a 1, call dfs on all 4 adjacencies until no more 1s are encounted
            - we now have an island
        - repeat this process for each index in the grid to ensire we find all islands
        - how to avoid counting multiple times? 
            - modify the input array to change 1s to 0s after visiting them
            - better method: keep a list of visited indexes, so we don't have side effects from modifying the input

        - time: n*m, since were gonna go through each index once
        - space: n*m for the max depth of the call stack
        """
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        visitedNodes = set()

        def dfsHelper(row, col):
            # out of bounds case
            if row not in range(ROWS) or col not in range(COLS):
                return

            # base case - value = 0 or already visited
            if grid[row][col] == '0' or (row,col) in visitedNodes:
                return

            # mark the current node as visited
            visitedNodes.add((row,col))

            # try each adjacency
            for adj in [[row, col+1], [row+1, col], [row-1, col], [row, col-1]]:
                dfsHelper(adj[0], adj[1])
        
        # we want to try each index in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visitedNodes:
                    result += 1
                    dfsHelper(r, c)

        return result
    
    """
    another solution using bfs
    """
    def numIslands2(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        visitedNodes = set()

        def bfs(row, col):
            # since its not recursive, we need a data structure for memory. typically we use a queue
            q = collections.deque()
            visitedNodes.add((row,col))
            q.append((row,col))

            # iterate through all possible adjacencies
            while q:
                node = q.popleft()
                row, col = node # deconstruct the tuple

                for r, c in [(row, col+1), (row+1, col), (row-1, col), (row, col-1)]:
                    # check if node is valid before adding it to the queue
                    if (r in range(ROWS) and c in range(COLS) and 
                    grid[r][c] == "1" and (r,c) not in visitedNodes):
                        q.append((r,c))
                        visitedNodes.add((r,c))

        # we want to try each index in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visitedNodes:
                    bfs(r, c)
                    result += 1

        return result