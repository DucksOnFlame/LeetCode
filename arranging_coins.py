import sys


class Solution(object):

    def arrangeCoins(self, n):
        rows = 0
        while n >= rows + 1:
            rows += 1
            n = n - rows
        return rows


solution = Solution()
print(solution.arrangeCoins(sys.maxsize))
