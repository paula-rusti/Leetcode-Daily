# 6 Aprilie 2023
"""
https://leetcode.com/problems/number-of-closed-islands/
"""
from typing import List


class Solution:
    def is_land(self, grid, i, j):
        return grid[i][j] == 0 if True else False

    def is_at_border(self, grid, i, j):
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            return True
        return False

    def dfs(self, grid, start_row, start_col) -> bool:
        # returns True if no cell that was at border was reached
        # returns False if while pushing the neighbours, a border cell was reached
        stack = [(start_row, start_col)]
        closed = True
        while len(stack) > 0:
            curr_row, curr_col = stack.pop()
            if (curr_row, curr_col) in self.visited:
                continue

            self.visited.add((curr_row, curr_col))
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
                    and self.is_land(grid, row, col)
                ):
                    stack.append((row, col))
        return closed

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()  # set of tuples
        islands = 0
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if (
                    self.is_land(grid, row_index, col_index)
                    and (row_index, col_index) not in self.visited
                    # and not self.is_at_border(grid, row_index, col_index)
                ):
                    print(f"starting dfs on coordintes {(row_index, col_index)}")
                    if self.dfs(grid, row_index, col_index):
                        print(
                            f"Counting island starting at coordinates ({row_index}, {col_index})"
                        )
                        islands += 1
        return islands


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]

    grid2 = [
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    ]  # output: 5

    grid3 = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    # output 1

    grid4 = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    # output 2

    sol = Solution()
    ans = sol.closedIsland(grid2)
    print(ans)
