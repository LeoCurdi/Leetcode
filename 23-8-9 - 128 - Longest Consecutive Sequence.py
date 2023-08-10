
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ 
            - Array is unsorted and we can't sort it as we need an o(N) solution
            - Turn the array into a set. Sets in python make it really 
              easy to check if an element is contained in it
            - For each num in the set, check if num - 1 exists. if not, then num is the start of a sequence
            - If num is the start of a sequence, check if 
              num + i exists and build the sequence until num + i doesn't exist 
        """
        # create a set for the initial arrray
        numSet = set(nums)
        # track result
        longest = 0
        # iterate through the list
        for n in nums:
            # if it's the start of a sequence
            if (n - 1) not in numSet:
                # then we know length is at least 1
                length = 1
                # build the sequence (while n + i exists the sequence is unbroken)
                while (n + length) in numSet:
                    # add length
                    length += 1
                # if we found a new longest set
                longest = max(longest, length) 
            # else - do nothing
        return longest

