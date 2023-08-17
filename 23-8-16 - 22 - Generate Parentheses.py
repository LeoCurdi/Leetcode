
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """ 
            - We're gonna use recursion with a stack
            - As we add parens, we'll track how many open and close ones 
              we have. We must make sure there are not more close than 
              opens and neither exceeds n.
            - The function will start by adding an open, then it can make 
              2 calls to add another open or a close. So basically each 
              time the helper is called, recursively add either just an 
              open or an open and a close if close is valid. This pattern will 
              continue until open and close reach n.
            - Note: you could do this without a stack and just create a new array
              each time a recursive call is made such that you will build every combo
              in it's own array. This would be o(N^2) space though.
            - Time is n*2 no matter what as we will have n*2 slutions. 
              Space is n since we will have around n recursive calls in 
              the call stack at a given time
        """
        # create stack and result
        stack = []
        result = []
        
        # create a recursive helper function (saves having to pass in stack and result)
        # the function will accept the amount of open and close parens
        def helper(openN, closeN):
            # if we've reached n open and close parens - we're done so add to result
            if openN == closeN == n:
                # add combo to result by extracting it from stack
                # take every char from the stack and join them together in an empty string
                combo = "".join(stack)
                # add the combo to the result list
                result.append(combo)
                # terminate the function
                return
            # we can only validly add a close if there are less closes than opens
            if closeN < openN:
                # add the close
                stack.append(')')
                # recursive call
                helper(openN, closeN + 1)
                # the above call will build all possible combinations with the newly 
                # added close paren and save them to result. So now that the
                # call has terminated we must pop it so we can continue to try with an open
                stack.pop()
            # and we want to add an open either way (we must still check that open has not exceeded n though)
            if openN < n:
                # add the open
                stack.append('(')
                # try all combos that start with the current set of parens
                helper(openN + 1, closeN)
                # remove the current paren
                stack.pop()

        # call the helper starting with 0 opens and closes
        helper(0, 0)
        # return the result
        return result

