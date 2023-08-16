
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        """ 
            - All we have to do is iterate through each char. If it's an 
              int, push it to the stack. If it's an operation, pop the 
              last 2 ints, use the operation on them, push the result 
              back to the stack.
            - Note: we're told the input is a valid expression so we dont
              need to check for invalid chars or order
        """
        # make a stack
        stack = []
        # iterate through the whole list of tokens
        for c in tokens:
            # if it's an operation - pop the last 2 values, 
            # use the op on them, push the result
            if c == '+':
                # get last 2 nums in reverse order
                num2 = stack.pop()
                num1 = stack.pop()
                # compute result
                result = num1 + num2
                # push result
                stack.append(result)
            elif c == '-':
                # get last 2 nums in reverse order
                num2 = stack.pop()
                num1 = stack.pop()
                # compute result
                result = num1 - num2
                # push result
                stack.append(result)
            elif c == '*':
                # get last 2 nums in reverse order
                num2 = stack.pop()
                num1 = stack.pop()
                # compute result
                result = num1 * num2
                # push result
                stack.append(result)
            elif c == '/':
                # get last 2 nums in reverse order
                num2 = stack.pop()
                num1 = stack.pop()
                # compute result. Note: result must be rounded toward zero
                #result = int(num1 / num2)
                #result = num1 // num2
                # the 2 lines above should both work for rounding but they dont cut it for this specific leetcode problem so we use the line below
                result = int(float(num1) / num2)
                # push result
                stack.append(result)
            # if it's an int - push it to the stack. 
            # Do this last bc checking if it's an int is hard
            else:
                # make sure to convert the string to an int
                stack.append(int(c))
        # return the final result
        return stack[0]

