class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        - given: an int array (may contain duplicates)
        - find: all possible subsets (the power set)

        - the solution set must not contain duplicate subsets

        - naive approach: do a backtracking decision tree, where each branch you chose to add or not add the current value
        - how to avoid generating duplicates?

        - modify the decision tree.
            - if we add num i to the left side, then the left tree contains all subsets containing at least one num i
            - thus, we dont need to add the i to the right side.
            - additionally, we must skip all occurrences of the num i on the right side.
                - this is hard, since the input array might not be sorted
            - sort the input array (nlogn). this doesnt contribute significantly to the time complexity
            - when branching right, skip past all occurences of the current value i

        - time: n * 2^n for generating 2^n subsets of up to length n
        """
        # sort the input
        nums.sort()

        result = []

        # passing in the current subset being built makes the code much cleaner
        def dfsHelper(i, subset):
            print("dfs called. i = ", i, "result = ", result)
            # base case: end of array
            if i >= len(nums):
                print("base case. result = ", result)
                result.append(subset[::]) # make a copy of the subset
                return

            # branch right: exlude the current i and all repeats of the value
            j = i
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j += 1
            dfsHelper(j+1, subset)

            # branch left: include the current i
            subset.append(nums[i])
            dfsHelper(i+1, subset)
            subset.pop()

        dfsHelper(0, [])
        return result