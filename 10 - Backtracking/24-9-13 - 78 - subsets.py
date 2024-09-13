class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        - given: an int array of unique elements
        - find: all possible subsets of the array (the power set)

        - use recursion for sure, so we don't have to calculate how many iterations it will take
        - all possible subsets of array [1..n] = all possible subsets of [2..n] + all possible subsets of [2..n] with 1 added to each of them
        
        - time: n (for n helper calls) * 2^n (first helper call is 1, next is 2, next is 4, next is 8 ... 2^n)
        """
        # start with an empty array
        result = [[]]
        if len(nums) == 0:
            return result

        def helper(index):
            # base case: we are at final index in array
            if index == len(nums) - 1:
                result.append([nums[index]])
                print("helper called", result)
                return
            # recurse to the end of the array
            helper(index + 1)
            # now take each value in the result, and make a copy of it with the current value added
            tempResult = result.copy()
            for r in tempResult:
                result.append([nums[index]] + r)

            print("helper called", result)

        helper(0)
        print(result)
        return result
    
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        more elegant solution (from Neetcode)
        - for each intex, we can choose to add it to the next subset, or not
        - draw a decision tree. ex [1,2,3] (left = dont add, right = add):
                           _
        1         _                 1
        2     _       2        1        12
        3 [[_] [3] [2] [23] [1] [13] [12][123]] = result

        - we have 2^n subsets
        - time: n * 2^n, since each subset can be up to n length
        """
        result, current = [], []

        def dfsHelper(index):
            # base case: end of array
            if index >= len(nums):
                # append the newly built subset
                result.append(current.copy()) # we need deep copies so we dont mess with the original memory for the results
                return
            
            # 2 paths: one for adding the current index, one for not adding it
            dfsHelper(index + 1)
            current.append(nums[index])
            dfsHelper(index + 1)
            current.pop()

        dfsHelper(0)
        return result
