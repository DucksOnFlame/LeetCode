class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)

        profit = 0

        for i in range(0, length - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit

print(Solution().maxProfit([0, 1, 5, 2, 2, 10, 20]))
