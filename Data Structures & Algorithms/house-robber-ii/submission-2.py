class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)

        def algo(li):
            dp = [0] * len(li)
            dp[0] = li[0]
            dp[1] = max(li[0], li[1])
    
            for i in range(2, len(li)):
                dp[i] = max(dp[i - 1], dp[i - 2] + li[i])

            return dp[-1]

        return max(algo(nums[1:]), algo(nums[:-1]))


        

        