class Solution(object):
    # 31 Martie 2023
    def check_valid(self, matrix):
        # check is a given piece is valid
        for row in matrix:
            if 'A' in row:
                return True
        return False

    def transpose_matrix(self, x):
        return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

    def is_cut_possible(self, matrix, row_cut):
        # checks is a row cut is possible at index row_cut
        top_valid = False
        for i in range(0, row_cut + 1):  # if we cut at index h_cut, row h_cut will be removed too
            if 'A' in matrix[i]:
                top_valid = True
                break
        bottom_valid = False
        for i in range(row_cut, len(matrix)):
            if 'A' in matrix[i]:
                bottom_valid = True
                break
        return top_valid and bottom_valid

    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        print(f"input matrix is {pizza}")
        if k > 1 and not self.check_valid(pizza):
            return 0

        if k == 1:  # if we need one pice ==> cannot cut anymore
            if self.check_valid(pizza):
                return 1
            else:
                return 0

        ans = 0
        for i in range(1, k):
            # check if we can do a row cut at index i
            if self.is_cut_possible(pizza, i):
                print(f"performing cut at row {i} for matrix {pizza}")
                ans += (self.ways(pizza[i:], k - 1))

            # check if we can do a column cut at index i
            transposed = self.transpose_matrix(pizza)
            if self.is_cut_possible(transposed, i):
                chopped_transposed = transposed[i:]
                print(f"performing cut at column {i} for matrix {transposed}")
                ans += (self.ways(self.transpose_matrix(chopped_transposed), k - 1))
        return ans

# TODO finish!!
if __name__ == '__main__':
    tc1 = (["A..", "AAA", "..."], 3)
    tc2 = (["A..", "AA.", "..."], 3)
    tc3 = (["A..", "A..", "..."], 1)
    tc4 = ([".A", ".."], 4)  # this fails

    sol = Solution()
    print(sol.ways(tc1[0], tc1[1]))
    # print(sol.ways(tc2[0], tc2[1]))
    # print(sol.ways(tc3[0], tc3[1]))
    # print(sol.ways(tc4[0], tc4[1]))
