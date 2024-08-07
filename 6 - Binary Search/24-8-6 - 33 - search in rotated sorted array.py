class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        - given: a sorted int array that has been rotated 1-n times, containing only unique elements
        - find: the index of a target (or -1 if target doesnt exist)

        - modified binary search
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            # middle >= left
            elif nums[middle] >= nums[left]:
                # if target is greater than middle or less than left then its to the right
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                # else its to the left
                else:
                    right = middle -1
            # middle < left
            else:
                # target is less than middle or greater than left, its to the left
                if target < nums[middle] or target > nums[left]:
                    right = middle - 1
                # target is greater than middle and less than left, its to the right
                else:
                    left = middle + 1
        return -1
