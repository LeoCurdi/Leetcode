class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        - given: 2 lists of ints
        - return: the index of the gas station you must start at to make it all the way around the circuit

        what we know:
        - there are n gas stations, n is the length of gas[]
        - the n gas stations make up a circular route
        - the amount of gas at station i is gas[i]
        - the car has an unlimited tank
        - cost[i] is the amount of gas to travel from station i to i+1
        - the car stats at one of the stations with an empty tank
        - must go clockwise
        - gauranteed to be 1 or 0 solutions

        intuition:
        - brute force:
            - try every possible starting point n*n
        - better:
            - we know we must at least start at a station that has enough gas to get to the next station
                - but these are not unique, and in some cases you might need to stock up multiple stations in a row
            - we need to get as much gas upfront as possible
                - greedy approach
            - if the sum of the cost is greater than the sum of available gas, there is no solution
                - but otherwise, there is definitely a solution, so we can check this right off the bat
            - model the gas stations as a list where the value is the gas gained
                - difference = amount picked up - amount spend to get to i+1
                - we need to find the maximum subarray, and start at the first index of it
                - the only problem is it could span from the right side of the array around to the left side
            - solution:
                - rule out whether theres a solution or not up front
                - keep track of total gas in tank
                - "try" position 0
                - if total ever goes negative, that position didnt work, try the next position
                    - we can skip trying positions between the failed one and the current index, since they will all fail
                - once we reach the end of the list and have a positive total, we know that start worked
                    - we already ruled out the possibility of no solution

        - time: linear, were only doing one pass
        - space: constant, not using extra space
        """
        # check if theres no solution
        if sum(gas) < sum(cost):
            return -1

        curStart = 0
        totalGas = 0

        # try positions until we can get to the end without total going negative
        for i in range(len(gas)):
            # update total
            totalGas += (gas[i] - cost[i])

            # check if it went negative
            if totalGas < 0:
                # rule out the (all) previous start
                curStart = i+1
                totalGas = 0

        # we know the total hasn't gone negative since the most recent start
        return curStart
