
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # we could set up an array to track frequency, or sort the nums, or use a hashset
        # we're gonna use a hashset
        # make a hashset
        hashset = set()
        # iterate through nums
        for num in nums:
            # check if num is already in the hash set
            if num in hashset:
                # if it is then we found a duplicate
                return True
            # add the number to the hashset
            hashset.add(n)
        # if we make it to the end, then there were no duplicates
        return False

