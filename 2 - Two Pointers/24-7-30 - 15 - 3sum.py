class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - given: array of ints
        - find: all unique sets of triplets of which the sum == 0
        - brute force: check each possible set of triplets - o(n3)
        - better: - o(n2)
            - sort the array - o(nlogn)
            - start with the leftmost element, and call sorted 2sum on the rest of the array with the complement of the leftmost as the target, recording the triplet if the sum == 0
            - shift to the second element and repeat (skip duplicates, and return once the element > 0, since no 2 positives can add up to 0)
        """
        result = []
        # sort the array
        nums.sort()
        # iterate through the array
        for i in range(0, len(nums) - 1):
            # check if i is a duplicate (avoid duplicate answers)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # if nums[i] > 0 - there can't be any more triplets with a sum of 0
            if nums[i] > 0:
                return result
            # run 2sum on the right portion of the array to find pairs that sum with i to equal 0
            left, right = i+1, len(nums) - 1
            while left < right:
                # compute the 3sum
                sum = nums[left] + nums[right] + nums[i]
                # case - sum = 0: record triplet of [i, l, r]
                if sum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    # now we have to update pointers because the while loop is still going so it can find all answers involving the same i
                    # as long as we update one pointer, the while loop will continue working without recording a dupe
                    right -= 1
                    while nums[right] == nums[right+1] and right >left:
                        right -= 1
                # case - sum of pair > 0: decrease right to lower the sum
                elif sum > nums[i]:
                    right -= 1
                # case - sum < 0: increase left
                else:
                    left += 1            
        return result
