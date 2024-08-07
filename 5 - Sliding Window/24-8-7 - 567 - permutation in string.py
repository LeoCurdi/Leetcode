class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - given: 2 strings
        - find: whether s2 has a substring that is a permutation (a reordering with the same chars) of s1

        - brute force: check all possible substrings of s2 against s1 in a hashmap to see if one has the same set of chars
        - better: use sliding window to do it in one pass, dropping and adding chars to the hashmap along the way
        """
        if len(s2) < len(s1):
            return False

        # insert all of s1 into a hashmap
        s1map = {}
        for c in s1:
            s1map[c] = 1 + s1map.get(c, 0)

        # create a window in s2 of s1's length
        left, right = 0, len(s1) - 1
        # insert the initial substring in s2 into a hashmap
        s2map = {}
        for c in range(right + 1):
            s2map[s2[c]] = 1 + s2map.get(s2[c], 0)
        
        # traverse s2 while checking each possible substring
        for r in range(len(s2)-right):
            # check if the maps match
            if s1map == s2map:
                return True
            # pop the prev char
            s2map[s2[left]] -= 1
            if s2map[s2[left]] == 0:
                del s2map[s2[left]]
            # adjust the window
            left += 1
            right += 1
            # add the next char
            s2map[s2[right]] = 1 + s2map.get(s2[right], 0)

        return s1map == s2map

        
