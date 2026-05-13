from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        
        for ky, v in sorted(c.items(), key=lambda item: item[1], reverse = True):
            res.append(ky)
            if len(res) >= k:
                break

        return res



        


