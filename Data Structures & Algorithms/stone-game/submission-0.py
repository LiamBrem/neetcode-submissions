class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(arr, aliceTurn):
            if not arr:
                return 0

            if (tuple(arr), aliceTurn) in dp:
                return dp[tuple(arr), aliceTurn]

            res = 0

            if aliceTurn:
                res = max(piles[0] + dfs(arr[1:], False), piles[-1] + dfs(arr[:-1], False))
            
            else:
                res = max(dfs(arr[1:], True), dfs(arr[:-1], True))

            dp[(tuple(arr), aliceTurn)] = res
            return res

            

        return dfs(piles, True) > 0
        