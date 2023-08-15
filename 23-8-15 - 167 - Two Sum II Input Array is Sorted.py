

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ 
            - We know numbers is sorted in ascending order and there is
              exactly 1 solution.
            - So we can make an infinite while loop that breaks out when we find the solution
        """
        # set up a left and right pointer
        l = 0
        r = len(numbers) - 1
        # make an infinite loop that short circuits if numbers is empty 
        # (we could actually just put while 1 since numbers cant be empty in this problem)
        while l < r:
            # if the sum is bigger than the target - decrease r
            if numbers[l] + numbers[r] > target:
                r -= 1
                # else if the sum is smaller than target - increase l
            elif numbers[l] + numbers[r] < target:
                l += 1
                # else (the sum equals target) - return solution
            else:
                return [l + 1, r + 1]

