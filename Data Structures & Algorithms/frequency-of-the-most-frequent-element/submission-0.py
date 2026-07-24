"""
- have k increment operations across nums
- what's the maximum frequency of the most frequent element after <= k operations

Ideas:
- greedily choose most numbers that are closest together
    - what if [100, 101, 99, 48, 57, 35, 60]
- sort numbers and find absolute values?
    - [101, 100, 99, 60, 57, 48, 35]
    - [1, 1, 39, 3, 11, 13]

"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 0
        cost = 0

        for r in range(len(nums)):
            cost += nums[r]

            while nums[r] * (r - l + 1) > cost + k:
                cost -= nums[l]
                l += 1

            res = max(res, r - l + 1)

        return res
            


        