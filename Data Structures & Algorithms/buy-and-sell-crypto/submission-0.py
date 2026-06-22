class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
            
        for price in prices[1:]:
            buy = min(buy, price)
            res = max(res, price - buy)

        return res
        