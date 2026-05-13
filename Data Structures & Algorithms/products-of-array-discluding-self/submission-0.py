class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = 1
        suff[-1] = 1

        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]
            
            j = len(nums) - i - 1
            suff[j] = nums[j + 1] * suff[j + 1]


        res = []
        for i in range(len(pref)):
            res.append(pref[i] * suff[i])

        return res


            