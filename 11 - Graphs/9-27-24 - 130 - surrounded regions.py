class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        - given: an m*n grid containing the chars 'X' and 'O'
        - find: all 'O' regions that are surrounded by 'X'. modify the board in place

        what we know:
        - a region is a group of Os that are connected (4-way adjacent to each other)
        - the region has to be completely surrounded by Xs
            - this means that edges don't count towards a region being surrounded, 
              thus any region that touches an edge cannot be surrounded
        - we need to detect all surrounded regions, and remove them from the board
            - by replacing the Os with Xs in place
        - we don't want to return anything

        intuition:
        - when you find a group, its either:
            - surrounded: meaning it's not touching an edge at all
            - not surrounded: part of the group is touching an edge somewhere
        - if the group is surrounded, remove it from the array
        - how to find groups? 
            - model the board as a graph, where adjacent cells are connected.
            - use dfs to discover the entire group
        - how to ensure we find all groups?
            - iterate the entire board
        - how to know if a group is surrounded? 
            - if we didn't find an edge
            - so if you find an edge, mark it as not surrounded, else assume surrounded
        - how to remove the group after dfs concludes?
            - save the nodes in a temporary group set
        - how to avoid repeated work?
            - mark nodes as visited

        - time: linear, we only need to visit each node once
        - space: linear, dfs call stack is upper bounded by the size of the grid
        """
        ROWS, COLS = len(board), len(board[0]) # easy way to start
        visited, currentGroup = set(), set()

        def dfsHelper(r, c):
            # base case: hit an edge
            if r not in range(ROWS) or c not in range(COLS):
                return False # return false for not surrounded
            
            # base case: already visited or its an X
            if (r,c) in visited or board[r][c] == 'X':
                return True
            
            visited.add((r,c))
            currentGroup.add((r,c))
            # branch to adjacencies
            isSurrounded = True # assume its surrounded, until proven o.w.
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]:
                res = dfsHelper(row,col)
                isSurrounded = isSurrounded and res
                # NOTE: I tried to do the above in one line, but it became a short-circuit evaluation issue when isSurrounded became false it wouldnt bother calling dfs

            return isSurrounded

        # iterate the board
        for r in range(ROWS):
            for c in range(COLS):
                # we only need to call dfs if its a O
                if board[r][c] == 'O' and (r,c) not in visited:
                    # discover the whole group
                    isSurrounded = dfsHelper(r, c)
                    # if the group we found is surrounded, remove it from the grid
                    if isSurrounded:
                        for row, col in currentGroup:
                            board[row][col] = 'X'
                    # clean up
                    currentGroup.clear()
        
        # don't return anything
        
    def solve2(self, board: List[List[str]]) -> None:
        """
        Neetcode approach:
            - only search for Os that are touching an edge, then dfs them to discover the entire group (which is unsurrounded)
                - mark all members with a T
            - after that, all remaining Os in the board must be members of a surrounded group, so just do a direct removal (no dfs)
            - then go back and change the Ts back to Os
        """
        ROWS, COLS = len(board), len(board[0])

        def dfsHelper(r, c):
            # base cases
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] == 'X':
                return
            
            # mark it T (we know its still part of an unsurrounded group)
            board[r][c] = 'T'
            
            # branch to adjacencies
            for row, col in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]:
                dfsHelper(row,col)


        # iterate the board for all unsurrounded groups
        for r in range(ROWS):
            for c in range(COLS):
                # if we found a node thats definitely part of an unsurrounded group
                if board[r][c] == 'O' and (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1):
                    dfsHelper(r,c)
                
        # remove all surrounded groups
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # undo all Ts
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'