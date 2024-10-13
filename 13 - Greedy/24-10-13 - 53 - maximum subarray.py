class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        - given: a list of ints
        - return: the sum of the subarray with the largest sum

        what we know:
        - there can be negative numbers, so a bigger subarray is not always better
        - a subarray has to be continuous, so you cant just pick elements from different parts of the list
        - the result cannot be negative, because if the entire list is negative, you would just pick an empty subarray
            - NOTE: leetcode actually wants a negative number returned in these cases

        intuition:
        - brute force n^2 alg
            - just try every possible sub array
        - better linear time alg 
            - sliding window approach
                - start with 2 pointers on the left side and move them right
            - keep track of the current subarray sum
            - if the current subarray sums to negative, it contributes nothing so we can just skip past it
            - keep checking for new max result
        - NOTE: we dont even need the left pointer, since were just saving the sum

        - time: linear for one pass
        - space: constant
        """
        res, curSum = float("-inf"), 0 # init result to -inf since leetcode wants to include negative results

        # traverse the list once
        #l = 0
        for r in range(len(nums)):
            # add the new value to the sum
            curSum += nums[r]

            # check for new result
            res = max(res, curSum)

            # if the current subarray is a net loss, skip it
            if curSum < 0:
                #l = r+1
                curSum = 0

        return res
