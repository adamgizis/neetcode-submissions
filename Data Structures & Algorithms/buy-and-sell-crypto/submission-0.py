class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gmin = prices[0]
        profit = 0
        for i in prices:
            if i - gmin > profit:
                profit = i -gmin
            gmin = min(i, gmin)
        return profit