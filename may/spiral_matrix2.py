# 10 mai
# https://leetcode.com/problems/spiral-matrix-ii/description/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cnt = 0

        top, bottom = 0, n - 1
        left, right = 0, n - 1

        # define the direction in which we will traverse the matrix
        direction = 'right'

        # initialize an empty list to store the traversal sequence
        generated_matrix = [[0 for _ in range(n)] for _ in range(n)]

        while left <= right and top <= bottom:
            if direction == 'right':
                for i in range(left, right + 1):
                    cnt += 1
                    generated_matrix[top][i] = cnt
                top += 1
                direction = 'down'

            elif direction == 'down':
                for i in range(top, bottom + 1):
                    cnt += 1
                    generated_matrix[i][right] = cnt
                right -= 1
                direction = 'left'

            elif direction == 'left':
                for i in range(right, left - 1, -1):
                    cnt += 1
                    generated_matrix[bottom][i] = cnt
                bottom -= 1
                direction = 'up'

            elif direction == 'up':
                for i in range(bottom, top - 1, -1):
                    cnt += 1
                    generated_matrix[i][left] = cnt
                left += 1
                direction = 'right'
        return generated_matrix


if __name__ == '__main__':
    pass
