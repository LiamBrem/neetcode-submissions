class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [] # [distance, [x, y]]

        def calcDistance(x, y):
            return math.sqrt(x**2 + y**2)

        distances = [[calcDistance(x, y), [x, y]] for x, y in points]
        heapq.heapify(distances)

        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res

        
        