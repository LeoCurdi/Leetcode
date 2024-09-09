class WordDictionary:
    """
    - design a data structure that supports adding and searching words
    - solution: use a trie (prefix tree) to easily search for words
    """

    """
    - initializes the object
    """
    def __init__(self):
        # just need to initialize the root
        self.root = TrieNode()
        
    """
    - given: a string
    - adds the string to the data structure
    """
    def addWord(self, word: str) -> None:
        cur = self.root
        # add each char of the string
        for c in word:
            # check if the char has already been inserted
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # mark the last char as the end of the word
        cur.endOfWord = True

    """
    - given: a string, the string may contain '.' which, can be matched to any char
    - finds: whether the string is contained in the data structure

    - since there may be multiple possibilities, we should use backtracking (recursion) dfs to explore all possible branches
    """
    def search(self, word: str) -> bool:
        # use a helper function
        def dfsHelper(cur, i):
            result = False # were going to OR in the result, so if any call returns true, the result will be true
        
            # base case: final char in word
            if i == len(word) - 1:
                # needs to match the char and be the end of the word
                if word[i] == '.':
                    for node in cur.children.values():
                        if node.endOfWord == True:
                            return True
                else:
                    if word[i] in cur.children:
                        return cur.children[word[i]].endOfWord == True
                return False

            # call dfs on each child of the current node that could match the searched word
            if word[i] == '.': # if '.', then any char counts (call dfs on all children)
                for node in cur.children.values():
                    result = result or dfsHelper(node, i + 1)
            else:
                if word[i] in cur.children:
                    result = result or dfsHelper(cur.children[word[i]], i+1)

            # return true if any of the dfs calls found a match
            return result
            
        # call dfs on the root
        return dfsHelper(self.root, 0)


# were gonna need a node class
class TrieNode:
    def __init__(self):
        # use a hashmap to access children in constant time
        self.children = {} # [key, val] = [char, nodePtr]
        self.endOfWord = False # mark nodes whether they mark the end of an inserted word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)