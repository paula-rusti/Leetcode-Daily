# 28 Martie 2023
from typing import List


class Solution(object):
    def minCostTicketsRecursive(self, i, days, costs):
        if i > max(days):
            return 0
        if i in days:
            return min(self.minCostTicketsRecursive(i+1, days, costs)+costs[0],
                        self.minCostTicketsRecursive(i+7, days, costs)+costs[1],
                        self.minCostTicketsRecursive(i+30, days, costs)+costs[2])
        else:
            return self.minCostTicketsRecursive(i+1, days, costs)  # dont have to travel this day then dont by a ticket

    def minCostTicketsMemoize(self, i: int, days: List[int], costs: List[int], min_cost: List[int]):
        # use a cost array to store the min costs of travelling each day
        # same as the recursive approach except that we query the min_cost array before recursively calling the function
        print(f"solving for i:{i}")
        if i > max(days):
            return 0

        if min_cost[i] != 0:
            print(f"using memoized value for subproblem i {i}")
            return min_cost[i]

        if i in days:
            ans = min(self.minCostTicketsMemoize(i+1, days, costs, min_cost)+costs[0],
                        self.minCostTicketsMemoize(i+7, days, costs, min_cost)+costs[1],
                        self.minCostTicketsMemoize(i+30, days, costs, min_cost)+costs[2])
        else:
            ans = self.minCostTicketsMemoize(i+1, days, costs, min_cost)  # dont have to travel this day then dont by a ticket

        min_cost[i] = ans   # store the solution to subproblem before returning from the recursive chain call
        return ans

    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # return self.minCostTicketsRecursive(days[0], days, costs)
        min_cost = [0] * 366   # min_cost[i] represents cost of travelling in days[i] day
        return self.minCostTicketsMemoize(days[0], days, costs, min_cost)



if __name__ == '__main__':
    days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
    # days = [1,2,3,4,5,6,7,8,9,10,30,31]
    # days = [1,4,6,7,8,20]
    costs = [2,7,15]
    sol = Solution()
    print(sol.mincostTickets(days, costs))

