class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # save the current minimum (left pointer)
        # as we iterate the right pointer, check for new minimums
        # each iteration of the right pointer, calculate current profit
        # overwrite max profit if necessary
        maxProfit = 0
        lowest = prices[0] # lowest is the left pointer
        # use for in loop for easier code
        for price in prices: # for each price in prices (this is the right pointer)
            # check for new lowest
            if price < left:
                left = price
            # compute the current profit
            currentProfit = price - lowest
            # if it is a new pax profit, overwrite it
            if currentProfit > maxProfit:
                maxProfit = currentProfit
        return maxProfit