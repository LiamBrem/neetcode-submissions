from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pq = []

        for ky, vl in c.items():
            heapq.heappush(pq, (-vl, ky))
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(pq)[1])

        return res



        


