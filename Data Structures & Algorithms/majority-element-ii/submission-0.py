from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        amt = len(nums) // 3
        res = []

        for key, value in c.items():
            if value > amt:
                res.append(key)


        return res

        
        