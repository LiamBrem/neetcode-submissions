"""
- no 2 same characters side by side
- return string or "" if impossible

Solution
- hash map with occurences (counter)
- iterate through starting with most frequent and interleave using max heap
- {a:3, b: 2, c: 1} -> abcaba

"""
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = [(-freq, letter) for letter, freq in c.items()]
        heapq.heapify(heap)
        prev = None

        if -heap[0][0] > (len(s) + 1) // 2:
            return ""

        res = ""

        while heap:
            freq, letter = heapq.heappop(heap)
            res += letter

            if prev: 
                heapq.heappush(heap, prev)

            if freq + 1 != 0:
                prev = (freq + 1, letter)
            else:
                prev = None

        return res


        


        