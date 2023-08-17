
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        """ 
            - This is kind of like the temperatures problem.
            - The difference is we will have an increaing stack rather 
              than decreasing.
            - Each time we encounter a rectangle, if it's higher or equal than 
              the previous one we push it to the stack, if it's lower we pop 
              previous ones until it is the highest. This is because when a rectangle
              has a shorter one to the right, we can't extend it into air space to make
              a bigger rectangle.  
            - We have to also keep track of indices so we can calculate area
              of rectangles when we pop something
            - Time: o(n) to iterate once over the whole input array
              Space: o(n) to make a stack containing up to n elements
        """
        # result is an integer
        result = 0
        # we need a stack
        stack = [] # [height, index]
        # for each height in heights
        for i, h in enumerate(heights):
            # we have to assign the start variable outside the while loop
            start = i
            # pop off all heights that are taller than current height
            while stack and stack[-1][0] > h:
                # get the most recent height (we get an array with height and it's index)
                heightPair = stack.pop()
                # calculate the area of the biggest rectangle that could be made with the height
                currentArea = heightPair[0] * (i - heightPair[1])
                # update result if necessary
                result = max(result, currentArea)
                # we have to save the index of where we stop popping from 
                # because lower heights can extend backwards
                start = heightPair[1]
            # always push the new height to the stack
            stack.append((h, start)) # use start because we want to extend backwards when possible, not just forward from their index
        # once we finish with all heights, there will likely be some left 
        # in the stack since we're only popping heights when we push a 
        # shorter one. Thus, we must compute recangle size with these as well.
        # iterate through the stack
        for h, i in stack: # [height, index]
            # compute area for the height (height * (end index - start index))
            currentArea = h * (len(heights) - i) # end index is always end of array for these
            # update result if necessary
            result = max(result, currentArea)
        return result

