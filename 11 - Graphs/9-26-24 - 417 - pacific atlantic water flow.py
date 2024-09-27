class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - given: an m*n grid representing an island bordering 2 oceans. 
                 the values of the cells rep the elevation above sea level.
                 when it rains, the water can flow to adjacent cells if they are lower
        - return: a list of coords of cells where rain water can flow to both oceans

        what we know:
        - water can only flow 4-way adjacently, so we can model the possible paths using a graph
        - pacific ocean is on the top and left sides of the array, atlantic ocean is on the right and bottom sides
            - so for a cell to satisfy the result, there has to be a downhill or flat path from the cell to both the top/left side and the bottom/right side
        - top right and bottom left cells automatically satisfy, since they are directly touching both oceans
            
        intuition:
        - inefficient solution (quadratic time):
            - for each cell, try every possible path to see if it can get to both oceans
        - better solution (cut out repeated work)
            - run dfs on each node, if a path reaches ocean x, propagate that back
            - if both oceans are propagated back to a node, that node can reach both so save it as a result
            - mark nodes as visited since we don't have to check them again
            
        - time: linear for one pass
        - space: linear for call stack

        - NOTE: this solution works for most cases, but not all. Also the code is disgusting. See better solution below
        """
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        reachedPacific, reachedAtlantic = set(), set()
        result = []

        def dfsHelper(r, c, prevHeight):
            # base case - reached ocean
            if (r < 0 or c < 0):
                return (True, False)
            if (r >= ROWS or c >= COLS):
                return (False, True)

            if (r,c) in visited:
                p, a = (r,c) in reachedPacific, (r,c) in reachedAtlantic
                return (p, a)
            
            if heights[r][c] > prevHeight:
                return (False, False)

            # call on adjacencies
            pacific, atlantic = False, False
            visited.add((r,c))
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]:
                p, a = dfsHelper(row, col, heights[r][c])
                pacific, atlantic = pacific or p, atlantic or a # or in the result
            
            if pacific:
                reachedPacific.add((r,c))
            if atlantic:
                reachedAtlantic.add((r,c))
            
            if pacific and atlantic:
                result.append([r,c])

            return [pacific, atlantic]

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    dfsHelper(r, c, float('inf'))


        return result
    
    
    def pacificAtlanticBetter(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - instead of checking each cell to see if it can reach both oceans:
        - start from ocean x and propagate inwards, marking all nodes that the ocean can reach in reverse
        - after doing that for both oceans, check which nodes both oceans touched
        """
        ROWS, COLS = len(heights), len(heights[0])
        reachedPacific, reachedAtlantic = set(), set()
        result = []

        def dfsHelper(r,c, visited, prevHeight):
            if (r not in range(ROWS) or c not in range(COLS)
                or (r,c) in visited or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]:
                dfsHelper(row, col, visited, heights[r][c])

        # call dfs on all pacific and atlantic touching nodes
        for c in range(COLS):
            dfsHelper(0, c, reachedPacific, heights[0][c])
            dfsHelper(ROWS-1, c, reachedAtlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            dfsHelper(r, 0, reachedPacific, heights[r][0])
            dfsHelper(r, COLS-1, reachedAtlantic, heights[r][COLS-1])

        # get the nodes that reached both oceans
        for r, c in reachedPacific:
            if (r,c) in reachedAtlantic:
                result.append([r,c])
        
        return result
