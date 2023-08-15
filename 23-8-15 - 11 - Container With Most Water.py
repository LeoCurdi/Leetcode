
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """ 
            - Brute force would be to try every possible combination of containers (n^2)
            - Better solution is to use left and right pointers and move pointers inwards
              toward the middle, checking for and recording new max areas. (n)
              We will compare l and r and shift whichever is smaller (this is the way to search for 
              higher values without skipping the true solution)
        """
        # make l and r pointers
        l = 0
        r = len(height) - 1
        # track the max area
        maxArea = 0
        # go until l meets r. at this point we can no longer find bigger containers
        while l < r:
            # compute the area - shortest height * distance between walls
            currentArea = min(height[l], height[r]) * (r - l)
            # check for new max area
            maxArea = max(maxArea, currentArea)
            # shift the shorter of the 2 walls
            # if left is shorter - shift left
            if height[l] < height[r]:
                l += 1
            # if right is shorter or they're equal - shift right (if equal you can shift either)
            else:
                r -= 1
        # return the max area
        return maxArea
