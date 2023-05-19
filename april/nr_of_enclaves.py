# 7 aprilie 2023
"""
https://leetcode.com/problems/number-of-enclaves/
"""
from typing import List


class Solution:
    def is_at_border(self, grid, i, j):
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            return True
        return False

    def dfs(self, grid, start_row, start_col) -> (bool, int):
        stack = [(start_row, start_col)]
        closed = True
        length = 0
        while len(stack) > 0:
            curr_row, curr_col = stack.pop()
            if (curr_row, curr_col) in self.visited:
                continue

            self.visited.add((curr_row, curr_col))
            length += 1
            print(
                f"visiting coordinates: {(curr_row, curr_col)} -> value: {(grid[curr_row][curr_col])}"
            )
            if self.is_at_border(grid, curr_row, curr_col):
                closed = False

            # Check adjacent cells
            for row, col in [
                (curr_row - 1, curr_col),
                (curr_row + 1, curr_col),
                (curr_row, curr_col - 1),
                (curr_row, curr_col + 1),
            ]:
                if (
                    0 <= row < len(grid)
                    and 0 <= col < len(grid[0])
                    and (row, col) not in self.visited
                    and grid[row][col] == 1
                ):
                    stack.append((row, col))
        return closed, length

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.visited = set()
        total_length = 0
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if (
                    grid[row_index][col_index] == 1
                    and (row_index, col_index) not in self.visited
                ):
                    print(f"starting dfs on coordintes {(row_index, col_index)}")
                    valid, length = self.dfs(grid, row_index, col_index)
                    if valid:
                        total_length += length
                        print(
                            f"Counting enclave starting at coordinates ({row_index}, {col_index})"
                        )
        return total_length


if __name__ == "__main__":
    # grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    sol = Solution()
    print(sol.numEnclaves(grid))
