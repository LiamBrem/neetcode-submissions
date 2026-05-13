from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pq =[(-vl, ky) for ky, vl in c.items()]
        heapq.heapify(pq)
        res = []
        
        for i in range(k):
            if pq:
                res.append(heapq.heappop(pq)[1])

        return res



        


