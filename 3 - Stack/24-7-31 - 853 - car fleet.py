class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - given: 2 arrays rep. car speeds and car starting positions and an int rep. end position,
          cars group together when a faster car reaches a slower car
        - find: the number of groups that pass through the target pos

        - the cars are like a system of linear eqs, if you graph their position over time then the intersections are when a car joins a fleet
        - cars are sorted by starting position, since they can never pass each other

        - traverse the list from largest start point to smallest
        - compute the ending time for each car
        - if the car i-1 ends sooner then car i, they become a fleet, so delete car i-1 and treat car i as the fleet
        - after traversing the list, the remaining cars rep the amount of fleets

        - time: nlogn for sorting, space: n for sorting and for the stack
        """
        # build an array of cars and sort it in decreasing order by start point
        cars = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            eta = float(target - p) / s # compute end time
            cars.append([p, s, eta])
        cars.sort(reverse=True)
        # to track fleets: instead of trying to remove certain cars from the array, just insert the fleet ones into a stack
        stack = []
        for p, s, eta in cars:
            # push the car, then check if it catches up to the fleet ahead of it
            stack.append(eta)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)