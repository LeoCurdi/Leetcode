class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        - given: array of sorted ints, target int
        - find: indices of 2 ints that add up to the target
        - brute force: check each possible pair
        - efficient: since array is sorted, one pass with left and right pointer 
        """
        left, right = 0, len(numbers) - 1
        # close in on middle
        while left < right:
            sum = numbers[left] + numbers[right]
            # case - sum = target: return indices
            if sum == target:
                return [left+1, right+1] # answer is not 0-indexed
            # case - sum of pair > target: decrease right to lower the sum
            elif sum > target:
                right -= 1
            # case - sum < target: increase left
            else:
                left += 1
        return