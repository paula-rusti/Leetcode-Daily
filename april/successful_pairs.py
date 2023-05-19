# 2 Aprilie 2023
from bisect import bisect_left

class Solution(object):
    def find_ge(self, a, x):
        'Find leftmost item greater than or equal to x'
        a.sort()
        i = bisect_left(a, x)
        if i != len(a):
            return i
        return -1

    def smallest_element_bigger_than_k(self, array, k):
        array.sort()
        bigger_or_equal_than_k = [i for i in array if i >= k]
        if len(bigger_or_equal_than_k) == 0:
            return -1
        res = min(bigger_or_equal_than_k)
        return array.index(res)

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # sort potions and for each spell find lower bound index (success/spell[index]) by using binary search
        ans = [0] * len(spells)
        potions.sort()
        for index, spell in enumerate(spells):
            if success % spell == 0:
                lower_bound = success // spell
            else:
                lower_bound = success // spell + 1
            lower_bound_index = self.find_ge(potions, lower_bound)
            if lower_bound_index != -1:
                ans[index] += (len(potions) - lower_bound_index)

        return ans


# TODO TLE on 51/56 test case
if __name__ == '__main__':
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    # pairs[i] is the number of potions that will form a successful pair with the ith spell.
    # output = [4, 0, 3]
    sol = Solution()
    ans = sol.successfulPairs(spells, potions, success)
    print(ans)
    # print(sol.find_ge([4, 2, 6, 8, 3, 2], 6))    # 2,2,3,4,6,8