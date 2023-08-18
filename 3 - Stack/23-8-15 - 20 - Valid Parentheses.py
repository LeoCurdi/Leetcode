
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """ 
            - Easiest way to solve this is with a stack. Every time you see 
              an opening parentheses you push it to the stack. Every time you
              see a closing parentheses you pop one from the stack and check if
              it corresponds.
            - iterate through the whole string and if something doesnt match 
              return false. If you make it to the end return true
            - Time = o(n), space = o(n)
        """
    # optimized solution - same as below but with a set of key value pairs to cut back on code duplication
        stack = []
        parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # iterate over the string
        for c in s:
            # if its an opening paren
            if c not in parentheses: # if it is not a KEY in parentheses
                # push it
                stack.append(c)
            # else it is a closing paren (we're assuming clean input)
            else:
                # if stack is empty or it doesnt correspond to the current top
                if not stack or stack[len(stack) - 1] != parentheses[c]:
                    # return false for invalid
                    return False
                # else it is valid so pop it
                stack.pop()
        # return true (but only if the stack is empty)
        return not stack


    # unoptimized solution - check each type of parens manually
        # create a stack (this can be done easily with an array o(1) for push and pop)
        stack = []
        # iterate over the string
        for c in s:
            # if it is an opening parentheses
            if c == '(' or c == '[' or c == '{':
                # push it to the stack
                stack.append(c)
            # else check each possible type of parentheses
            # this could be optimized with a set of key value pairs
            elif c == ')':
                # check if the top of the stack corresponds
                # short circuit to see if stack is empty
                if not stack or stack[len(stack) - 1] != '(':
                    # we have a mismatch so return false
                    return False
                # top of stack corresponds so pop it
                stack.pop()
            elif c == ']':
                # check if the top of the stack corresponds
                # short circuit to see if stack is empty
                if not stack or stack[len(stack) - 1] != '[':
                    # we have a mismatch so return false
                    return False
                # top of stack corresponds so pop it
                stack.pop()
            elif c == '}':
                # check if the top of the stack corresponds
                # short circuit to see if stack is empty
                if not stack or stack[len(stack) - 1] != '{':
                    # we have a mismatch so return false
                    return False
                # top of stack corresponds so pop it
                stack.pop()
        # return true (but only if the stack is empty)
        return not stack
            


