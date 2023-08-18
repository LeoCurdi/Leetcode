
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ we're gauranteed exactly 1 solution so we dont need to check for no solution or mulitple.
            Naive solution is to check every number against every other number O(n^2).
            Sorting would be NlogN but then we wont be able to return the correct indices of the result.
            So we'll make a hashmap of all values in the array and then we can instantly check if each 
            number has a corresponding number that will work - o(n) time and space
        """
        # create a hashmap
        # we dont need to add all values to the hashmap initially, we can do it as we go, since we can't reuse the same value twice anyways
        hashmap = {} # value: index
        # loop through each element
        for i, n in enumerate(nums): # this gives the index and the value stored at the index
            # calculate the complementary value
            difference = target - n
            # if the complementary value is in the hashmap, we know they add up to the target and we have a solution
            if difference in hashmap:
                # return the indices of the solution
                return [hashmap[difference], i] # hashmap[value] = complementary index, i = current index
            # add the value to the hashmap
            hashmap[n] = i # hashmap[value] = index

