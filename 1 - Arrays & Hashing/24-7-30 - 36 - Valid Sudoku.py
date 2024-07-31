
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """ 
            - use a hashset / dictionary for each row, col, and grid
            - easy to check for duplicates in a hashset
            - inserting and checking is done in constant time, so total is linear time and space on size of grid
        """
        cols = collections.defaultdict(set) # key = 0-8, value = 9 sets, each rep. a list of all present numbers in one col
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set) # key = (0-2,0-2) to rep a 3 by 3 of sub grids

        # traverse the input grid in one lap - inserting to all 3 hashsets each iteration
        for r in range(9):
            for c in range(9):
                # case - empty index - do nothing
                if board[r][c] == '.': 
                    continue
                # case - dupe encountered - return false
                if (
                     # check the row, col, and subgrid for if the element has already been inserted
                     board[r][c] in rows[r]
                     or board[r][c] in cols[c]
                     or board[r][c] in grids[(r // 3), (c // 3)]
                ):
                    return False
                # insert number into the 3 sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grids[(r // 3), (c // 3)].add(board[r][c]) # get the grid (0-2,0-2) from the row and col 0-8
        return True
