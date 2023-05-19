# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# 18 mai
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> list[int]:
        # build adjacency list
        adjacency_list = defaultdict(list)
        for src, dest in edges:
            adjacency_list[src].append(dest)

        reachable = set()
        for key in adjacency_list:
            reachable.update(set(adjacency_list[key]))

        return list(set(adjacency_list.keys()) - reachable)