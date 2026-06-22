from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [-val for val in c.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                num = 1 + heapq.heappop(heap)
                if num != 0:
                    q.append((num, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0]) 


        return time
        