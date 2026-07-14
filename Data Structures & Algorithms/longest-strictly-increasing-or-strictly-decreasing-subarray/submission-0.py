class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0

        while l < len(nums):
            r = l + 1
            while r < len(nums) and nums[r] > nums[r - 1]:
                r += 1

            res = max(res, r - l)
            l = r

          
        l = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums) and nums[r] < nums[r - 1]:
                r += 1

            res = max(res, r - l)
            l = r
  

        return res
            
        