
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """ 
            - We're gonna start from left and right and work towards the middle.
              We keep track of the highest wall on the left side and right side.
              Each time we move in, if the new wall is higher we update highest wall for the side,
              else we know there's water accumulation so we add it to the total
        """
        # left and right ptrs
        l = 0
        r = len(height) - 1
        # set up left max and right max variables
        leftMax = height[l]
        rightMax = height[r]
        # variable for accumulating total water volume
        totalVolume = 0
        # loop toward the center
        while l < r:
            # move the lower of the left and right walls
            # if left max is lower - move left in
            if leftMax < rightMax:
                # move left in
                l += 1
                # if new left is higher than max - update max
                if height[l] > leftMax:
                    leftMax = height[l]
                # else if new left is lower than left max - we have water so add it
                # (we know there's water because we already checked left max < right max)
                elif height[l] < leftMax:
                    # add the amount of water that can fit (the vertical drop from left max to current left)
                    totalVolume += leftMax - height[l]
                # else (left max = current left) - do nothing
            # if right is lower or they're equal - move right in (similar to container with most water problem)
            else:
                # move right in
                r -= 1
                # if new right is higher than max - update max
                if height[r] > rightMax:
                    rightMax = height[r]
                # else if new right is lower than right max - we have water so add it
                # (we know there's water because we already checked left max < right max)
                elif height[r] < rightMax:
                    # add the amount of water that can fit (the vertical drop from right max to current right)
                    totalVolume += rightMax - height[r]
                # else (right max = current right) - do nothing
        # return total volume
        return totalVolume






        """ 
            Note: tried to do a sliding window approach.
            Almost got it but gave up because of edge cases and went with a left and right ptr approach
        """
"""         l = 0
        r = 1
        totalVolume = 0
        while l < len(height) - 1:
            while height[l] > height[r]:
                r += 1
            newVolume = 0
            tempHeight = height[l]
            while l < r:
                l += 1
                newVolume += tempHeight - height[l]

            totalVolume += newVolume
            l = r
            r += 1 """
