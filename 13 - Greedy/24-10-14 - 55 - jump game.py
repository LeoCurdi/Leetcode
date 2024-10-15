class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        - given: a list of ints
        - return: whether you can reach the end index

        what we know:
        - you start at the first index
        - the value at the current index is how far you can jump
            - you can jump less though
        - we dont need to find the fastest way, we just need to know if there's a way
        - values can be 0, so there may not be a way
        - values cannot be negative

        intuition:
        - brute force:
            - could try every possible path, but this is super inefficient k^n, where k is the average value of the list
        - efficient:
            - we only need to check if you can clear all the 0s, since any positive values will gaurantee passage to the next index at least
            - start from the end and work backwards
            - if we hit a 0
                - need to find a jump over it
                - increment the jump distance while traversing back until we find a value that can clear the 0
                - if another 0 is encounted while searching
                    - ignore it, any value that can clear the far 0 will also clear the close 0
                - if we reach the left side and didnt clear it, return false

        - time: linear for one pass
        - space: constant, not using any extra memory
        """
        jump = 0 # track the jump required to clear the current 0

        # iterate backwards through the list
        for i in range(len(nums)-2, -1, -1): # skip the rightmost index
            # if we need to clear a 0
            if jump > 0:
                # check if we can clear it from this index, else add to jump distance
                if nums[i] >= jump:
                    jump = 0
                else:
                    jump += 1

            # else, if the current index is a 0, mark that we must make a jump
            elif nums[i] == 0:
                jump = 2

        # if we reach the left side and have a jump that wasnt cleared, return false
        return jump == 0
