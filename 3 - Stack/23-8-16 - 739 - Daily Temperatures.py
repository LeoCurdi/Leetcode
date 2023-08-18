
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """ 
            - Stack will be in monotonic decreasing order
            - Start by pushing the first temp to the stack. Then, if the next
              temp is greater than the prev temp, record 1 in result and pop
              the prev temp from the stack. If the new temp is lower than prev,
              just push it to the stack. This means the stack will always be in 
              decreaing order
            - The trick is we have to keep track of the index of each day
              when it is inserted into the stack. That way when we find a 
              higher temp we know how many days it's been
        """
        # create a result array and default all the values to 0
        result = [0] * len(temperatures)
        # create a stack which will be a 2D array - [temp, index]
        stack = []
        # for each value in temperatures
        for i, t in enumerate(temperatures): # get index and value using enumerate
            """ 
                I noticed in the commented code below that we're pushing every temp
                to the stack, so the if-else is pointless and we can refactor
                * Just make sure the new temp is being pushed after we pop and process
                  lower temps 
            """
            # while new temp is higher than stack top - pop and record difference in days (indexes)
            while stack and t > stack[-1][0]:
                # pop the top array of temp and index
                tempPair = stack.pop()
                # record the result for that day (result = current index - index of day temp was recorded)
                result[tempPair[1]] = i - tempPair[1]
            # push the latest temp to the stack always
            stack.append((t, i)) # push a pair

            
            # if stack is empty or if current temp is lower than prev temp - just push new temp
"""             if not stack or t < stack[-1][0]:
                # push the temp and the index together to the stack
                stack.append((t, i))
            # else (temp is higher tha prev) - we must pop and record days
            else:
                # we'll need a while loop in case new temp is high enough that we can pop multiple days
                while stack and t > stack[-1][0]:
                    # pop and save the temp / index array
                    tempPair = stack.pop()
                    # we've found a higher temp so record the amount of days it took
                    # result[index of day] = current index - index of day
                    result[tempPair[1]] = i - tempPair[1]
                # we have to make sure we still append the new temp to the stack.
                # otherwise it will be skipped and result for that day will never be recorded
                stack.append((t, i)) """
        # return the result
        return result







