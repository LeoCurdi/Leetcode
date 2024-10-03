class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        - given: a beginning word, an end word, a list of available words
        - return: the length of the shortest transformation sequence from begin to end

        what we know:
        - a transformation sequence is a sequence of words where
            - the words are from the input word list
            - every adjacent pair of words in the sequence differs by exactly one letter
        - all words are the same length
        - the end word must be in the word list for the sequence to count
        - all words are unique
        - the length of a transformation equals the number of words in it (including start and end)
        - if there is no possible transformation from beginWord to endWord, return 0

        intuition:
        - if we start thinking about how to come up with the possible transformation paths, it leads us to a decision tree
            - start at the first word, then branch off for each word in the input that could be the next in the sequence
            - this way we discover all possible solutions, and just return the length of the shortest one
            - problem: this is 2^n * k time complexity, since each additional word in the input doubles the amount of possible paths and words are length k
        - better solution:
            - we can take advantage of the fact that adjacent words can only differ by 1 char
            - for any word in the input, we can map it to all words that differ by 1 char
                - ex: hot can map to *ot, h*t, or ho*, where * is any letter a-z
                - you could put *ot in the hashmap and map it to all words that can replace the *
                    - do this for h*t and ho* as well
            - once we generate the map, we can perform a graph search to find the shortest path
                - bfs is a good way to find a shortest path
            - NOTE: when drawing the decision tree, you can cut out redundant edges such that each word only appears once in the graph
            - the graph is now n nodes, with n^2 possible edges

        - time: n*m*n to generate the map
        - space:
        """
        # edge case
        if endWord not in wordList:
            return 0
        
        neighbors = collections.defaultdict(list) # create a dictionary full of empty lists as default values
        wordList.append(beginWord)

        # build the neighbors map
        for word in wordList:
            # for each pattern (ex hot -> *ot, h*t, or ho*)
            for k in range(len(word)):
                pattern = word[:k] + "*" + word[k+1:]
                neighbors[pattern].append(word) # this word satisfies the pattern we just derived from the word

        visited = set([beginWord])
        q = deque([beginWord])
        result = 1

        # perform bfs traversal
        while q:
            # traverse the next level
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                # queue up the valid neighbors
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            result += 1

        return 0 # we didnt find a path