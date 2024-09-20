class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        - given: a string containing digits from 2-9
        - find: all possible combinations of letters that you could represent with the digits 
        
        what we know
        - digits are mapped to letters like you see on a pin pad (2->abc, 3->def, ..., 9->wxyz)
        - answers can be in any order, but since combinations must be in the order of the digits
        
        intuition
        - using a decision tree:
            - we can take digit i as the ith level of the tree
            - for each node, make a new branch for each letter the next digit could rep
        - create the decision tree with a dfs recursive alg

        - time: n * 3.75^n for generating 3.75^n combinations (there are 3.75 letters avg per digit) of length n
        - space: n * 3.75^n for the space taken by the result
        - space excluding result: n for the recursive call stack of n depth
        """
        # we need to create a mapping of digits to letters
        phonePadMap= {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []

        def dfsHelper(i, cur):
            # base case: end of input
            if i == len(digits):
                # add the result (dont add empty results)
                if len(cur):
                    result.append(cur)
                return

            # branch for each letter in the digit map
            for c in phonePadMap[digits[i]]:
                dfsHelper(i+1, cur + c)

        dfsHelper(0, "")
        return result