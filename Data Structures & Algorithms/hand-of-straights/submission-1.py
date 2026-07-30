"""
- hand[i] = value on card

- rearrange cards into groups sized 'groupSize'
- cards are consecutively increasing by 1
- true if cards can be arranged that way, false otherwise

----
- min heap storing (num, occurences)
- add to an addBack list after each groupSize is met
or

counter + minHeap
addBack to heap if counter is > 0


"""
from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        heap = list(c.keys())
        heapq.heapify(heap)

        while heap:
            addBack = []
            for i in range(groupSize):
                if len(heap) == 0:
                    return False

                next = heapq.heappop(heap)
                c[next] -= 1

                if addBack and next - addBack[-1] != 1:
                    return False

                addBack.append(next)

            for val in addBack:
                if c[val] > 0:
                    heapq.heappush(heap, val)


        return True 

        