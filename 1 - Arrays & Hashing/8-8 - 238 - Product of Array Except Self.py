
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ 
            - must be o(N) and we cant use the division operator
            - we're going to use a prefix and post fix strategy where we
              calculate the product of nums before i an nums after i.
              This can be done in linear time as we can run through nums
              to get the prefixes while saving them in result array, then 
              run through nums in reverse getting the postfixes and multiply 
              them by the corresponging prefixes in the result array
              - this is o(1) space because we're storing prefix in the result array which is a freebie)
        """
        # create a result array of same length as nums and fill it with 1's as a default 
        # (default doesnt really matter since we will ovwrwhite it with prefix)
        result = [1] * (len(nums))
        # default the prefix to 1 for multiplication purposes
        prefix = 1
        # calculate the prefix for each i in nums
        for i in range(len(nums)):
            # save the prefix to the corresponding result index
            result[i] = prefix
            # calculate the prefix for the next num
            prefix *= nums[i]
        # default the postfix to 1 for multiplication purposes
        postfix = 1
        # calculate the postfix for each i in nums - we must iterate backwards to do this
        for i in range(len(nums) - 1, -1, -1):
            # calculate the final result for the num by multiplying prefix by postfix
            result[i] *= postfix
            # calculate next postfix
            postfix *= nums[i]
        return result

