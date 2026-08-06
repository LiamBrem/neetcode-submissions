class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            newStart, newEnd = newInterval
            start, end = interval

            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]

            elif newStart > end:
                res.append(interval)

            else:
                newInterval = [min(start, newStart), max(end, newEnd)]



        res.append(newInterval)
        return res


        

        