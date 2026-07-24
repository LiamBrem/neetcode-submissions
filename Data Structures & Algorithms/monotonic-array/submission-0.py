class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        res = True

        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                res = False
                break

        if res:
            return True

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                return False

        return True

        