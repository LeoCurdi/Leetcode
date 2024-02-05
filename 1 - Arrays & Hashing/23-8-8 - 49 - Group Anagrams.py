
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """ 
            One way to solve this would be to sort each string in the list which would make all the 
            anagrams have the same order but thats M*NlogN (bad).
            Better solution: M*N
                - use a frequency counter to count the characters in each string
                - insert each string into a hashmap, using the frequency counter for that string as the key
                - any anagrams will have the identical frequency counters and will be inserted at the same key in the hashmap
                - thus we end up with an object (the hashmap) containing arrays which each contain groups of strings that are anagrams
        """
        #resultMap = {} # count: string
        resultMap = collections.defaultdict(list) # we have to initialize any missing keys with the default value 'list', this protects against an edge case where the string is empty and thus so is count
        # go through every string in the input
        for s in strs:
            # create an frequency counter array with 26 zeros
            count = [0] * 26
            # go through every character in the string and count how many of each character
            for c in s:
                # we want to map a to index 0 and z to index 25
                # so take the ascii value of the character, and subtract the ascii value of a to get the target index
                # and add 1 to that index, such that the character is counted
                count[ord(c) - ord('a')] += 1 # (we we're given that all letters are lowercase)
            # insert the string into the hashmap using the string's char count as the key
            # count is an array (list in python), which cannot be a key, so we change it to a tuple (this is a weird python thing)
            resultMap[tuple(count)].append(s)
        # we dont need the keys anymore we just want to return the values, so turn the object to an array
        return resultMap.values() # this will return each value in the object in an array