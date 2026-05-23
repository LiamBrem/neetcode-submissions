class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                stackTemp, stackIdx = s.pop()
                res[stackIdx] = i - stackIdx
            
            s.append((t, i))

        return res