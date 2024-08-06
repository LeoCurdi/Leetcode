class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - given: a sorted int array that has been rotated 1-n times, containing only unique elements
        - find: the min element in the array

        - modified binary search
            - array[left] is always higher than array[right], until left reaches the min
            - if middle > right, move to the right half
            - if middle < right, move to the left half
        """
        left, right = 0, len(nums) -1
        
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        
        # left meets right at the min
        return nums[left]