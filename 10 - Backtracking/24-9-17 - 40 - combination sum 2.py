class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - given: an array of nums, a target num
        - find: all unique combinations where the nums sum to the target

        - what we know:
            - each num in the array may only be used once
            - the solution must not contain duplicates
            - the input array may contain duplicates
            - all values in the array are positive (if they werent, it would effect the alg)

        - intuition:
            - use a decision tree (dfs backtracking approach)
            - create every possible combo, filter out any that add up to greater than target
            - but: since the input may contain dupes, we end up with dupe results
            - how to avoid dupe results? if a number i is added to the left subtree,
              then all combos containing at least 1 occurence of i will be in the left subtree,
              so dont add any occurences of i to the right subtree
            - to do this the array must be sorted - easy nlogn, doesn't impact overall complexity
            - once sorted, we can use indexing to skip over duplicate values when recursing to the right subtree

        - time: n * 2^n for 2^n possible combinations upper bounded by length n
        - space: n * 2*n for 2*n possible combinations
        - space not counting result: n for the recursive stack of up to n depth
        """
        result = []
        candidates.sort()

        def dfsHelper(i, curNums, curSum):
            # base case: curSum == target
            if curSum == target:
                result.append(curNums.copy()) # create a deep copy, so we don't mess it up later
                return
            # base case: end of array or curSum is already greater than the target
            if i >= len(candidates) or curSum > target:
                return
            
            # branch left - add the current val
            curNums.append(candidates[i])
            dfsHelper(i+1, curNums, curSum + candidates[i])
            curNums.pop()

            # branch right - skip the current val, plus all future occurences of it
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfsHelper(i+1, curNums, curSum)
        
        dfsHelper(0, [], 0)
        return result