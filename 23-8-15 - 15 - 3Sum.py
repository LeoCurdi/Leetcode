
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """ 
            - The only efficient way to solve this without getting
              duplicates is to sort the input array (nlogn)
            - We're going to solve 2sum for each element in the array, using the 
              inverse of the element as the target, and the rest of the array 
              to the right of the element as the input array. (n^2)
            - First we must sort the array to prevent getting duplicate solutions (nlogn)

        """
        # create a result array
        result = []
        # sort the input array (nlogn)
        nums.sort()
        # for each value in the input array - use the value as the first num in the combo and call 2sum to find the other 2 nums
        for i, a in enumerate(nums): # index and value
            # we can optimize this by skipping any first num that is positive, because we know that positives wont cancel out to 0
            if a > 0:
                # once we get to positives, we're done with the whole function becuase we wont find any more 3sums
                break # break out of the loop

            # if we've already used this value as the first num in a solution
            # since input is sorted, just check if there's 2 of the same num in a row
            if i > 0 and a == nums[i - 1]: # throw in a short circuit to avoid checking nums[-1]
                # skip it entirely
                continue # this will skip to the next iteration of the loop
            # now solve 2sum on the num
            # set up left and right pointer
            l = i + 1
            r = len(nums) - 1
            # loop through until we find a solution that works with the current first num or l = r
            while l < r:
                # a + nums[l] + nums[r] must = 0 to have a 3sum
                # so nums[l] + nums[r] must = -a
                cur = nums[l] + nums[r]
                # if cur is greater than -a - cur must decrease
                if cur > -a:
                    # so get a smaller third element
                    r -= 1
                # if cur < -a - cur must get bigger
                elif cur < -a:
                    # get a bigger second element
                    l += 1
                # else (cur = -a aka cur + a = 0) - thats a solution
                else:
                    # add an array with the solution to the list of solutions
                    result.append([a, nums[l], nums[r]])
                    # now that we got a solution, we have to move l and r so we dont infinitely record the same solution
                    l += 1
                    r -= 1
                    # we also have to make sure that if the next 2 nums are the same, that we wont record a duplicate solution
                    # this is a bit of a trick
                    while nums[l] == nums[l - 1] and l < r:
                        # we can just keep shifting l in this case
                        l += 1
        return result
