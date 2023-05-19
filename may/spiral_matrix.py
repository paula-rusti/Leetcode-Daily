# https://leetcode.com/problems/spiral-matrix/
# 9 mai 2023
from typing import List


class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        pass
        # order: right, down, left, up

        # define the boundaries of the matrix
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1

        # define the direction in which we will traverse the matrix
        direction = 'right'

        # initialize an empty list to store the traversal sequence
        traversal = []

        while left <= right and top <= bottom:
            if direction == 'right':
                for i in range(left, right + 1):
                    traversal.append(mat[top][i])
                top += 1
                direction = 'down'

            elif direction == 'down':
                for i in range(top, bottom + 1):
                    traversal.append(mat[i][right])
                right -= 1
                direction = 'left'

            elif direction == 'left':
                for i in range(right, left - 1, -1):
                    traversal.append(mat[bottom][i])
                bottom -= 1
                direction = 'up'

            elif direction == 'up':
                for i in range(bottom, top - 1, -1):
                    traversal.append(mat[i][left])
                left += 1
                direction = 'right'
        return traversal


if __name__ == '__main__':
    # Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    sol = Solution()
    print(sol.spiralOrder(mat))