"""
temperatures on the ith day

result[i] = number of days after i before warmer temp (no day = 0)

brute force:
- for each i - loop until finding a warmer day
- O(n^2)

optimal:
- stack: iterate backward?
- strictly decreasing
- 


[40, 38, ]

[30,38,30,36,39,40,28]

[1, 4, 1, 1, 1, 0, 0]

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while s and temp > s[-1][0]:
                stackTemp, stackIdx = s.pop()
                res[stackIdx] = i - stackIdx

            s.append((temp, i))


        return res

        