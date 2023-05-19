# 5 aprilie 2023
"""
You are given a 0-indexed array nums comprising of n non-negative integers.
In one operation, you must:
Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.
"""
import math
from typing import List
class Solution(object):
    def procedure(self, nums, index) -> List[int]:
        # index > 1
        nums[index] -= 1
        nums[index - 1] += 1
        return nums

    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = nums[0]
        for i, el in enumerate(nums):
            maxx = max(maxx, math.ceil(sum(nums[:i])/(i+1)) )
        return maxx


    def minimizeArrayValue_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dummy approach: choose max and store min for the initial max, then asses their difference
        # ==> TLE on testcase 26/68
        initial_max = max(nums)
        initial_max_index = nums.index(initial_max)
        initial_min = min(nums)

        if initial_max_index < 1:
            return initial_max  # cannot decrease its predecessor

        while initial_min <= initial_max:
            if initial_max_index < 1:
                break
            nums = self.procedure(nums, initial_max_index)
            initial_min = min(nums)
            initial_max = max(nums)
            initial_max_index = nums.index(initial_max)
        return initial_max


if __name__ == '__main__':
    # nums = [7, 1, 3, 9, 11, 6, 8, 9]
    nums = [10, 1]
    sol = Solution()
    print(sol.minimizeArrayValue(nums))
