class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        - given: an array of unique intergers
        - find: all possible permutations

        - what is a permutation? a rearrangement of all the values in a set / list
        - so all permutations must be the length of the input
        - how many permutations are there for a set of n length? n factorial (n!)

        - intuition:
            - we can use a decision tree to generate all possible orderings
            - how to ensure we dont use the same num twice?
                - keep track of the current path
            - this is hard to do recursively, because the subproblem isnt clear
                - for a length 3 array, there is a different subproblem for each index
            
        - approach:
            - subproblem: all permutations of array [0..n] = all permutations of array [1..n], with 0 added to each position in each of the permutations
            - recurse to the end of the array (base case = empty array)
            - add the current index val to each position in each permutation added from the inner recursive call
            - return back to the outer recursive call

        - time: (n^2) * n!, for n! possible permutations of length n, where inserting each element into potentially the middle takes n time
        - space: n * n! for building n! perms of length n
        """
        result = []

        def dfsHelper(index):
            # base case
            if index == len(nums):
                result.append([])
                return
            
            # recurse down
            dfsHelper(index + 1)

            # create new permutations with current val
            resultTemp = result.copy() # use this for taking a snapshot of the result
            for p in resultTemp: # for each permutation
                for i in range(len(p) + 1): # create new ones with the current val at each possible position
                    pNewI = p.copy() # create a new permutation
                    pNewI.insert(i, nums[index]) # insert num at index i
                    result.append(pNewI)   
                result.remove(p) # pop p    

        dfsHelper(0)
        return result
    
    
    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        """
        since we didnt have to branch in the recursive function, we know we could also do it iteratively
        """
        result = [[]] # base case

        for n in nums:
            newPerms = []
            for p in result:
                for i in range(len(p) + 1):
                    pNew = p.copy()
                    pNew.insert(i, n)
                    newPerms.append(pNew)
            result = newPerms 

        return result
