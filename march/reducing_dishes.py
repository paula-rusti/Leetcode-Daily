class Solution(object):
    # 29 Martie 2023
    def computeCoef(self, array):
        sum = 0
        for index, element in enumerate(array):
            sum += (element*(index+1))
        return sum

    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        negatives = [x for x in satisfaction if x < 0]
        positives = [x for x in satisfaction if x >= 0]

        negatives.sort(reverse=True)
        positives.sort()

        minCoef = self.computeCoef(positives)
        if len(negatives) == 0:
            return minCoef
        minSum = sum(positives)

        maxx = minCoef
        for e in negatives:
            currentSum = minSum + e
            if minCoef+currentSum >= maxx:
                maxx = minCoef+currentSum
                minCoef = maxx
                minSum = currentSum
        return maxx


if __name__ == '__main__':
    satisfaction = [-1,-4,-5]
    sol = Solution()
    print(sol.maxSatisfaction(satisfaction))


