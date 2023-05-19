# 3 Aprilie 2023
"""You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person."""


class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        start_index = 0
        end_index = len(people) - 1
        pairs = 0
        while start_index <= end_index:
            pairs += 1
            if people[start_index] + people[end_index] <= limit:
                start_index += 1
            end_index -= 1
        return pairs
