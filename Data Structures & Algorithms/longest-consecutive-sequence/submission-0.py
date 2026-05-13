class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums: # start
                i = 1
                while num + i in nums:
                    i += 1
                
                longest = max(longest, i)

        
        return longest





        