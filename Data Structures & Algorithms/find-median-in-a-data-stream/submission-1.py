"""
- 2 heaps
- smaller - >= (max heap)
- bigger - (min heap)
"""
class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        if self.larger and num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)

        # balance
        if len(self.smaller) - len(self.larger) > 1:
            move = -heapq.heappop(self.smaller)
            heapq.heappush(self.larger, move)
        elif len(self.larger) - len(self.smaller) > 0:
            move = -heapq.heappop(self.larger)
            heapq.heappush(self.smaller, move)


    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        else:
            return -self.smaller[0]
        
        