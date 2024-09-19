class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        - given: a string s
        - return: a set of all partitions of s, st each piece of the partition is a palindrome

        - what we know:
            - partition: a way of dividing the string into parts. ex: aab -> [a, ab] or [a, a, b]
            - palindrome: a string that can be reversed and still be the same
            - s contains only lowecase a-z

        - intuition:
            - we at least need to generate all the possible palindromes that sat. the condition, 
              so there's no trick to do this efficiently.
            - generate all possible partitions:
                - use decision tree to branch left or right. left = split cur index, right = dont split it
            - with all possible partitions, check every substring of each to see if its a palindrome.
            - but, we can at least try to avoid generating partitions that wont satisfy
                - while partitioning, track the current substring
                - when finishing a substring, if its not a palindrome, throw away the partition
                - if you get to the end of the array without tossing the partition, save it as a result
        """
        result = []

        def dfsHelper(i, curSubStr, curPartition):
            # base case - end of string
            if i >= len(s) - 1:
                curSubStr = curSubStr + s[i]
                # we still need to add the current substr
                if self.isPalindrome(curSubStr):
                    curPartition.append(curSubStr)
                    result.append(curPartition.copy()) # only add result if the partition is ok
                    curPartition.pop() # cleanup
                return

            # add the current index to the current substr
            curSubStr = curSubStr + s[i]

            # branch left - split the partition here, check if its even a valid palindrome
            if self.isPalindrome(curSubStr):
                curPartition.append(curSubStr)
                dfsHelper(i+1, "", curPartition)
                curPartition.pop() # clean up

            # branch right
            dfsHelper(i+1, curSubStr, curPartition)
        
        dfsHelper(0, "", [])
        return result

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
    
    
    def partition(self, s: str) -> List[List[str]]:
        """
        - alternate solution (Neetcode)

        - to generate partitions:
            - get the first substring, which well need to try every length from just the first char, to the entire string
            - then append that with the result of partitioning the remainder of the string
        - were basically just trying every substring and skipping the ones that aren't palindromes
        """
        result, partition = [], []

        def dfs(i):
            # base case
            if i >= len(s):
                result.append(partition.copy())
                return
            
            # iterate through the remainder of the string
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop() # clean up

        dfs(0)
        return result