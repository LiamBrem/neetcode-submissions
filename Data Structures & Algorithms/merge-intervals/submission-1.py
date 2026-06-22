class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            currStart, currEnd = res[-1]
            if start > currEnd:
                res.append([start, end])
            elif end > currEnd:
                res[-1][1] = end


        return res
        