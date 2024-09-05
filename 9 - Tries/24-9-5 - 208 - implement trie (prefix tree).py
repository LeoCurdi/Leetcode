class Trie:
    """
    A trie (aka a prefix tree) is a tree data structure that can efficiently store and retrieve keys in a dataset of strings
    The purpose of a trie is the "starts with" ability that no other data structure can do efficiently

    - in this case, our trie only needs to support lowercase a-z
        - this means our trie nodes will each have up to 26 children
    """
    def __init__(self):
        # all we need is an emptry tree
        # the root node can't contain a letter
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        # start at the root
        cur = self.root

        # for every char in the word
        for c in word:
            # insert the char into the trie (unless it's already in)
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # traverse down by 1 char
            cur = cur.children[c]

        # mark the final char as the end of a word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        # traverse down, char by char
        for c in word:
            # if the char hasnt even been inserted, then the word is not in the trie
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # if the node for the final char of the word is marked as end of word, then the word is in the trie
        return cur.endOfWord == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        # traverse down, char by char
        for c in prefix:
            # if the char hasnt even been inserted, then the prefix is not in the trie
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # if we made it this far, either the prefix itself is a word in the trie, or its a prefix of a word in the trie
        return True

"""
we cant have a trie without trie nodes
"""
class TrieNode:
    def __init__(self):
        self.children = {} # store children nodes in a hashmap (there will be up to 26)
        self.endOfWord = False # so we can mark a node as the end of a word that's been inserted
        # the value of the current node is stored in the hashmap of the parent

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)