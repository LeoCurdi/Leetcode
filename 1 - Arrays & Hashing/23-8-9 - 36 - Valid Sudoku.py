
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """ 
            - we're going to make a hashset for each row, column, and square 
              to check if there are any duplicates present.
              Inserting into a hashset is o(1) so we have o(N) with n being 9*9
            - Note: we could also use arrays instead of hashsets since we know the dimentions of the sudoku board
            - Then loop through the sudoku board once, insert everything into 
              all 3 hashsets simultaniously, and check as we go if there is a duplicate.
            - if so, return false. else, continue to the end and return true
        """
        # create 3 hashsets. A hashset is like a 2D array
        cols = collections.defaultdict(set) # key = column 0-8, value = list of all values in the column
        rows = collections.defaultdict(set) # key = row 0-8
        squares = collections.defaultdict(set) # key = (r/3, c/3) - this will give us (0-2, 0-2) which tells us which square we're in
        # iterate through each row
        for r in range(9):
            # for each row, iterate through each element (column)
            for c in range(9):
                # if slot is empty - do nothing
                if board[r][c] == '.':
                    continue
                # else, if we've found a duplicate - return false immediately
                if (
                    # check if the element is already in the row, col, or square
                    board[r][c] in rows[r] # rows[r] returns a list of elements that are in the row
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3), (c // 3)] # must do integer division here (we have squares (0-2, 0-2) integers only)
                ):
                    return False
                # else - insert the value into all 3 hashsets and continue to the next value
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # if we made it to the end that means there were no duplicates so return true
        return True
