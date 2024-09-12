class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word):
        cur = self.root
        # iterate the word
        for c in word:
            # if the char isnt in the trie: insert it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # mark end
        cur.endOfWord = True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def findWordsBetter(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        - given: an m * n board of chars, a list of strings
        - find: all the strings that are on the board. strings can consist of a series of adjacent chars, no repeats in the same string
        
        - better solution: prefix tree
            - insert the given words into a prefix tree
            - call dfs backtracking on the entire grid, checking if the current word is in the prefix tree
                - if not, end the branch of dfs
            - this eliminates duplicate work st we can be finding multiple words at the same time
        """
        # insert all words into a prefix tree
        prefixTree = Trie()
        for word in words:
            prefixTree.insertWord(word)
            
        # easy way to start - get the dimensions
        ROWS, COLS = len(board), len(board[0])
        result = set()
        path = set() # prevent a word from repeating the same coords

        # need a dfs helper function
        def dfsHelper(row, col, cur, accumulatedWord):
            # base cases
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return
            if (row, col) in path:
                return
            if board[row][col] not in cur.children:
                return
            
            # call dfs on adjacent chars, update path, update accumulated word
            path.add((row, col))
            cur = cur.children[board[row][col]]
            accumulatedWord += board[row][col]
            if cur.endOfWord:
                result.add(accumulatedWord)
            dfsHelper(row+1, col, cur, accumulatedWord)
            dfsHelper(row-1, col, cur, accumulatedWord)
            dfsHelper(row, col+1, cur, accumulatedWord)
            dfsHelper(row, col-1, cur, accumulatedWord)
            path.remove((row, col))

        # call the modified word search on each possible starting point (the entire grid)
        for i in range(ROWS):
            for j in range(COLS):
                dfsHelper(i, j, prefixTree.root, "")

        # cast the result from a set to a list before returning it
        result = list(result)
        return result



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        - given: an m * n board of chars, a list of strings
        - find: all the strings that are on the board. strings can consist of a series of adjacent chars, no repeats in the same string
        
        - brute force: use solution for word search 1, and repeat it for each word in the list

        - this is too slow of an approach
        - time: o(k * (n*m) * 4^l), where k is the number of words, n*m is the size of the grid, and l is the average length of a word
        """

        # the solution for word search 1. returns a bool
        def singleWordSearch(word):
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
        
        # code for multiple words
        result = []

        # call single word search for each word
        for word in words:
            # if the word is found - add it to the result
            if singleWordSearch(word):
                result.append(word)

        return result
