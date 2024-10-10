class Solution:
    def climbStairs(self, n: int) -> int:
        """
        - given: a in int n for number of steps in a staircase
        - return: how many distinct ways you can climb to the top

        what we know:
        - you can climb 1 or 2 steps at a time
        - we start on 0, and the last step gets us to n
        - if were 1 step from n, taking 2 steps doesnt count as a separate way, since it would go past n

        intuition:
        - we can visualize the possible ways as a decision tree
        - brute force:
            - use the decision tree approach to recursively generate all 2^n possible paths
            - exclude the ones that end on n+1
            - return the sum
        - the brute force apporach is 2^n very bad
        - but we dont even need to generate all possible paths, we just need to know how many there are
        - if you compute the results for the first 5 values of n, it becomes clear that its just a fibonacci sequence
        - numPaths(n) = numPaths(n-1) + numPaths(n-2)
            - makes sense, bc when you add one to n, all of the paths to n-1 can now get to n with one step,
              and all the paths to n-2 can get to n with 2 steps
        - using this pattern, we just need to know what the previous 2 values were
            - use DP to cache the result (memoization)
            - also, we dont even need to store all results, just the prev 2, so we can make the space constant

        - time: linear on n, since each value up to n is a simple calculation
        - space: linear for the DP array, but constant since were only storing last 2 vals
        """
        i1, i2 = 1, 1
        cur = 1

        for i in range(2, n+1):
            cur = i1 + i2
            i2 = i1
            i1 = cur

        return cur

