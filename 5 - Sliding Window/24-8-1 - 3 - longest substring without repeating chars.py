class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        - given: a string
        - find: the length of the longest substring without repeating chars

        - bad alg: check every possible substring
        - better: use a one-pass sliding window approach, with a hashset each iteration to check a specific substring for duplicates
        
        - time: n because its one pass
        - space: n because we could add the whole string to the set
        """
        result = 0
        l, r = 0, 0
        tempSet = set()
        
        while l < len(s):
            # check if the new char is already in the set to check for dupes
            # if dupes, shift l until the dupes are eliminated, and remove from the set
            while s[r] in tempSet:
                tempSet.remove(s[l])
                l += 1
            # insert new char and shift r
            tempSet.add(s[r])
            if r < len(s) - 1:
                r += 1

            # record length
            result = max(r - l, result)

        return result