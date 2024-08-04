class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        - standard binary search alg
        """
        # repeat until left and right meet at the target
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        return -1
