# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# 23 may
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.stream = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.stream) < self.size:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:
            heapq.heapreplace(self.stream, val)
        return self.stream[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)