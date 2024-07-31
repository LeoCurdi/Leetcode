class Solution:
    def twoSum(self, nums: List[int], target: int):
        """
        - given: array of ints and a target int
        - find: the indices of the 2 ints that add up to the target
        - only one solution per input
        - brute force: check each possible pair
        - efficient: use a hashmap
            - for each element, there is only one other value that could add with it to equal the target
            - so use a hashmap (value, index) of the input to check if the complement exists in the array in constant time
            - insert each element after checking it to avoid edge cases, the answer will be found when the latter of the pair is encountered
        """
        hashMap = {} # value, index
        # interate through the input in one pass
        for i in range(0, len(nums)):
            # compute the complement of the current element
            difference = target - nums[i]
            # check if the compelement has been inserted into the map
            if difference in hashMap:
                # return the indices of the pair
                return [hashMap[difference], i]
            # insert the current element
            hashMap[nums[i]] = i
        return

