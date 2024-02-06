class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        - given: 
            *an array of ints in sorted order
            *a target integer
        - if target exists, return index, else return -1
        - TIME CONSTRAINT: must be O(logN) (so use binary search)
        - Note: some variation of binary search is a common interview problem

        """
        # create a left and right pointer
        l = 0
        r = len(nums) - 1

        # while left and r haven't met (they will meet at the target if it exists)
        while l <= r:
            # compute middle index (midpoint between left and right)
            m = l + ((r - l) // 2) # integer division
            # target is to the left
            if target < nums[m]:
                # move right to m
                r = m - 1
            # target is to the right
            elif target > nums[m]:
                # move left to m
                l = m + 1
            # found target
            else:
                return m # return index of target
        # didnt find target
        return -1