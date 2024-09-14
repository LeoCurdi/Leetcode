class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - given: an array of unique ints, a target int
        - find: a list of all unique combinations in the array, that sum to the target

        - the same number in the array can be used multiple times to form a combination
        - array is not sorted
        
        - brute force approach: try every possible combination, check the sum
        - were pretty much going to use brute force for this problem, with some optimizations
            - use a decision tree (dfs backtracking)
            - dont continue down paths where the sum is already >= the target
            - modify the dfs to prevent duplicates
                - left path adds nums[i], then the tree in right path can only ever add nums[>i]

        - time: 2^t, where t is the target value
        """
        result, currentPath = [], []

        # we cant add numbers before index i, to avoid duplicates
        def dfsHelper(i, curSum):
            print(currentPath)
            # base case: current index out of range or the current combination sum > target
            if len(candidates) <= i or curSum > target:
                return
            # found a valid combo
            if curSum == target:
                print("found a result: ", currentPath)
                result.append(currentPath.copy()) # save a deep copy to the result array, so we dont overwrite the memory
                return

            # explore left and right paths
            currentPath.append(candidates[i]) # add i to left subtree
            dfsHelper(i, (curSum + candidates[i])) # dont increase i, since left subtree may continue adding the same value
            currentPath.pop() # dont add i to right subtree
            dfsHelper(i+1, curSum)

        dfsHelper(0, 0)
        return result