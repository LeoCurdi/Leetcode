class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        - given: an integer n
        - find: all distinct solutions to the n-queens puzzle

        what we know
        - the n-queens puzzle:
            - given an n*n chessboard
            - place n queens on the board s.t. none of the queens attack each other
            - queens can move up/down, left/right, diagonal, up to 7 squares
        - the answer can be returned in any order
        - do we need to factor in for when the board is greater than 7 squares long (size can be 1-9)? no. were assuming these queens can move infinite distance
        
        inutition
        - there can't be multiple queens in the same row or column
        - there also cant be multiple queens in the same diagonal
        - if we just try every possible layout, we will get all possible solutions
        - how to try every layout?
            - use backtracking approach (decision tree)
            - start with the first row
            - for each possible position for a queen in that row (only 1 queen per row):
                - dfs branch and repeat for the remainder of the board
            - if any layout is satisfying at the end, add it to the result
        - we need to construct the solution as we go
        - how to check if its valid?
            - rows are valid automatically, since were only putting 1 queen per row
            - cols are easy to check - just make sure there isnt already a queen in the column were inserting into
            - diagonals are tricky - we have to check all up-right diagonals and down-right diagonals
                - for decreasing diagonals, doing (row - col) gives you the same constant for each square in the diagonal
                - for increasing diagonals, doing (row + col) gives you the same constant for each square in the diagonal
            - we can efficiently check if a row/col/diagonal is occupied using a hashset
        
        - time: n^n, for n*n*... possible solutions to try
        - space (excluding result): n, for n-depth recursive call stack
        """
        cols, increasingDiag, decreasingDiag = set(), set(), set()
        result = []
        board = [["."] * n for i in range(n)] # initialize a board for the solution

        def dfsHelper(row):
            # base case - out of rows
            if row == n:
                # if we made it to the end, we already know the solution is valid
                copy = board.copy() # make a deep copy of the board
                copy = ["".join(row) for row in board] # format it in the required way (join each row into a string)
                result.append(copy) 
                return

            # try a branch for each position in the current row
            for col in range(n):
                # skip if we cant insert the queen here
                if col in cols or (row + col) in increasingDiag or (row - col) in decreasingDiag:
                    continue
                # insert queen
                board[row][col] = "Q"
                cols.add(col)
                increasingDiag.add(row + col)
                decreasingDiag.add(row - col)
                # branch
                dfsHelper(row+1)
                # clean up
                board[row][col] = "."
                cols.remove(col)
                increasingDiag.remove(row + col)
                decreasingDiag.remove(row - col)
            
        dfsHelper(0)
        return result