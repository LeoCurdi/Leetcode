class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        - given: an integer n
        - find: all possible correct combinations of n pairs of standard parens
        
        - for a combo to be correct, you just need to have as many or more opens than closes at any point from left to right
        
        - since were esentially building a tree of possible combos, use recursion
            - if open == close -> add an open
            - if open > close -> add an open and a close
            - if open == n -> add closes until close == n
        - use a stack to contain a combo while its being generated
        """
        comboStack = []
        result = []

        def helper(openNum: int, closeNum: int):
            # base case - finished a combo
            if openNum == closeNum == n:
                result.append("".join(comboStack)) # generate a string from the combo
                return
            # case - we can add an open
            if openNum < n:
                comboStack.append("(")
                helper(openNum +1, closeNum)
                comboStack.pop()
            # case - we can add a close
            if openNum > closeNum:
                comboStack.append(")")
                helper(openNum, closeNum +1)
                comboStack.pop()
        
        helper(0, 0)
        return result