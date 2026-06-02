from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr = [(-value, key) for key, value in c.items()]
        heapq.heapify(arr)
        res = []

        for i in range(k):
            res.append(heapq.heappop(arr)[1])

        return res

        
        


        


