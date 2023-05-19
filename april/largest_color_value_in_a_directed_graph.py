# 9 April
"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Hint1: use topological sort:
    linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.
    only possible for directed acyclic graphs
___________
Hint2: let dp[u][c] := the maximum count of vertices with color c of any path starting from vertex u.
___________
topological sort approach:
Create a stack to store the nodes.
Initialize visited array of size N to keep the record of visited nodes.
Run a loop from 0 till N
    if the node is not marked True in visited array
        Call the recursive function for topological sort and perform the following steps.
            Mark the current node as True in the visited array.
            Run a loop on all the nodes which has a directed edge to the current node
                if the node is not marked True in the visited array:
                    Recursively call the topological sort function on the node
            Push the current node in the stack.
Print all the elements in the stack.
"""
from typing import List


class Solution:
    def __init__(self):
        pass

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        pass

    def build_adj_list(self, edges, n):
        adj_list = dict({i: [] for i in range(n)})
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
        return adj_list

    def topo_sort_util(self, node, graph, stack, visited):
        """
        :param node: current node
        :param graph: adjacency list of the graph
        :param stack:  stack of nodes pushed so far
        :param visited: visited array
        :return: No return, just modifies tack and visited array
        """
        visited[node] = True    # mark current node as visited
        for vecin in graph[node]:
            if not visited[vecin]:
                self.topo_sort_util(vecin, graph, stack, visited)
        stack.append(node)


    def topo_sort(self, graph, n):
        """
            n -> nr of nodes
            graph -> adjacency list of the graph
        """
        visited = [0] * n
        nodes = []
        for i in range(n):
            if not visited[i]:
                self.topo_sort_util(i, graph, nodes, visited)
        return nodes[::-1]


if __name__ == '__main__':
    sol = Solution()
    adj = sol.build_adj_list(edges=[ [5,0], [5,2], [4,0], [4,1], [2,3], [3,1] ], n=6)
    print(sol.topo_sort(adj, 6))
    # Input: colors = "abaca", edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    # Output: 3

