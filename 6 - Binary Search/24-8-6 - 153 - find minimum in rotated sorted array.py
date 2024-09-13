class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - given: a sorted int array that has been rotated 1-n times, containing only unique elements
        - find: the min element in the array

        - modified binary search
            - array[left] is always higher than array[right], until left reaches the min
            - if middle > right, move to the right half
            - if middle < right, move to the left half
        - NOTE: if middle lands directly on the minimum, we could miss it, so we need to continuously save middle as a possible min
        """
        left, right = 0, len(nums) -1
        curMin = float("Inf")

        while left < right:
            middle = (left + right) // 2
            curMin = min(curMin, nums[middle]) # check if middle is a new min

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        
        # left meets right at the min
        return min(nums[left], curMin)