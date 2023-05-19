# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# 17 may
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # transform the linked list to an array
        arr = []

        # Traverse the linked list and append each value to the array
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        m = n // 2

        left_half = arr[:m]
        right_half = arr[m:]
        right_half = right_half[::-1]

        print(arr)
        print(left_half)
        print(right_half)

        sums = [x + y for x, y in zip(left_half, right_half)]
        return max(sums)
