
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        """
            - the cars can all be represented on a 2D graph as linear equations
              with time on the x-axis and poision on the y-axis. So position
              is the y-intercept and speed is the slope
            - When you graph out all the cars you can see when cars intersect 
              and the number of fleets is apparent in the graph
            - So we could just compute all intersections and if an intersection
              is before position 12 we know its a fleet. This would be o(n^2) though.
            - Instead we can sort the cars in order by position, start at the closest
              car to the end, and work backwards, checking if cars will catch up, then
              popping the ones that do (while keeping the front car). The front car will
              represent the fleet and this works because any car that catches up will
              reduce it's speed to that of the front car
            - Time is o(nlogn) for sorting and space is o(n) for the stack
        """
        # for ease, we're going to merge the speed and position arrays into an array of pairs. (we could have also used a hashmap with index being position)
        # make an array and fill it with arrays of position and speed for each item in position and speed using zip
        # this is called list comprehension in python
        cars = []
        # this is too confusing so i refactored it below
"""         for p, s in zip(position, speed):
            cars.append([p, s]) """
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        # sort the pairs in reverse order
        cars.sort(reverse = True)
        # create a stack to track fleets
        stack = []
        # for each car
        for p, s in cars: # get position and speed
            # calculate what time the car will reach the destination
            eta = float(target - p) / s # Note: time may be a decimal
            # push the eta of the car no matter what because a car by itself is a fleet
            stack.append(eta)
            # now that we've added the car, we want to know if it will catch up to the one in front if it
            # so check if the time will overlap (but only if there is another fleet)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # if it catches up then pop it as it will merge and become part of the fleet in front
                stack.pop()
        # return the number of fleets aka length of stack
        return len(stack)




