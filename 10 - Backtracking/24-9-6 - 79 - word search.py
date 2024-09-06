class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        - given: an m by n grid of chars, a string
        - find: whether the string exists in the grid. 
        
        - the string can make turns within the board, but cant be diagonal
        - we cant re-use any chars

        - no super efficient solution, just go through each possibility using backtracking
        
        - time: o(n * m * 4^len(word))
        """
        # easy way to start - get the dimensions
        ROWS, COLS = len(board), len(board[0])

        # keep track of the path to avoid repeating chars
        path = set() # use a set of coords (sets dont allow duplicates)

        # use dfs to check each possibility
        def dfsHelper(row, col, i): # pass in position on board and position in the given word
            # base case - end of word
            if i == len(word):
                return True
            # out of bounds case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return False
            # case: char on board doesnt satisfy the word
            if board[row][col] != word[i]:
                return False
            # case: current pos has already been visited
            if (row, col) in path:
                return False
            
            # call dfs on each adjacent element
            i += 1
            path.add((row,col))
            result = (dfsHelper(row-1,col,i) or
                    dfsHelper(row+1,col,i) or 
                    dfsHelper(row,col-1,i) or 
                    dfsHelper(row,col+1,i))
            path.remove((row,col)) # important cleanup step - otherwise all the dfs calls will mess each other up
            
            # return True if one of the dfs calls found the word
            return result
        
        # we need to call dfs on each letter in the grid that could be the start of the word
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    path.clear() # reset the path to empty
                    if dfsHelper(i, j, 0):
                        return True
        # if none of the starts led to the full word
        return False
