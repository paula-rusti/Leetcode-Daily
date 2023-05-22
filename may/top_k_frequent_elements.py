# 22 may
# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        for x in nums:
            if x in hash_set:
                hash_set[x] += 1
            else:
                hash_set[x] = 1
        hash_set = {k: v for k, v in sorted(hash_set.items(), key=lambda item: item[1])}
        return list(hash_set.keys())[::-1][:k]