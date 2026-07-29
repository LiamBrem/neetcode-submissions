from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        @lru_cache(None)
        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if holding:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)
                return max(sell, hold)

            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                return max(buy, skip)

        return dfs(0, False)