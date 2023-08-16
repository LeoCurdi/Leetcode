
class MinStack(object):
    """ 
        - We're going to make 2 stacks. The first one is the main stack, and
          the second one is going to store the current minimum value each time 
          a value is inserted to the main stack.
    """
    def __init__(self):
        # create 2 stacks
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # push the value to the stack
        self.stack.append(val)
        # determine new current min
        # if there is a prev min
        if self.minStack:
            # get prev min
            prevMin = self.minStack[-1] # this is like [len(self.minStack) - 1]
            # if new val is smaller than prev min make it cur min else keep prev min
            curMin = min(val, prevMin)
        # if there is not a prev min
        else:
            # make new val the cur min
            curMin = val
        # the following line is shorthand for the whole if else above (it's kind of ridiculous to look at though)
        #curMin = min(val, self.minStack[-1] if self.minStack else val)
        # push the current min to the min stack
        self.minStack.append(curMin)

        
    def pop(self):
        """
        :rtype: None
        """
        # pop the top item from the stack
        self.stack.pop()
        # pop the corresponding current min from min stack
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # return the top value in the stack
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # return the current min (top value in min stack)
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()